from math import ceil

from flask import render_template, session, redirect, make_response, request, url_for, flash, jsonify
from io import BytesIO
from modules.scholar import scholar_blue
from modules.scholar.forms import SearchForm, RegisterForm
from modules.scholar.forms import LoginForm
from modules.scholar.utils import get_verify_code
from modules.common import graph_list, scholar_log_req, es
from modules.scholar.models import User, Researcher
from app import db
import random
import json


@scholar_blue.route("/index", methods=["GET", "POST"])
@scholar_log_req
def index():
    seed = random.randint(0, 300)
    query = {
        "query": {
            "function_score": {
                "functions": [
                    {
                        "random_score":  {
                            "seed": seed
                        }
                    }
                ],
                "score_mode": "sum",
            }
        },
        "size": 10
    }
    result = es.search(index='scholar', doc_type='teacherInfo', body=query)
    res_dict = result['hits']['hits']

    form = SearchForm()
    if form.validate_on_submit():
        data = form.data
        print("searchData", data)
        if data['searchInput'] is not None:
            return redirect(url_for("scholar.entities", keyword=data['searchInput'], page=1))
    return render_template("search/index.html", search_items=res_dict, form=form)


@scholar_blue.route("/", methods=["GET", "POST"])
@scholar_blue.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        data = form.data
        # print(list(session.items()))
        # print("I am here", form.data)
        # {'account': 'root', 'pwd': 'root', 'verify_code': 'utas', 'submit': True,
        # 'csrf_token': 'IjBhZGE4Zjc1YmE2MWJlNmI4ZDliOTY3NTRmMGQ2ODQ3MmEzNGQ3ZmYi.YJC1HQ.TNuDjDz-cGqt1f1BUVdCOn-ixCI'}
        usr_count = User.query.filter_by(username=data['account']).first()
        if usr_count is None:
            flash("账号错误！", "danger")
            return redirect(url_for("scholar.login"))
        if not usr_count.check_pwd(data['pwd']):
            flash("密码错误！", "danger")
            return redirect(url_for("scholar.login"))
        if session.get('image').lower() != form.verify_code.data.lower():
            flash('验证码错误！', "danger")
            return redirect(url_for("scholar.login"))
        session["admin"] = data['account']
        # print(session)
        return redirect(request.args.get("next") or url_for("scholar.index"))
    return render_template("login/login.html", form=form)


# 注销路由
@scholar_blue.route('/logout')
@scholar_log_req
def logout():
    session.pop('admin', None)
    return redirect(url_for("scholar.login"))


# 注册路由
@scholar_blue.route("/register", methods=["GET", "POST"])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        data = form.data
        if data['pwd'] != data['repeat_pwd']:
            flash("两次填写的密码不一致！")
            return redirect(url_for("scholar.register"))
        if session.get('image').lower() != form.verify_code.data.lower():
            flash('验证码错误！', "danger")
            return redirect(url_for("scholar.register"))
        names = User.query.filter_by(username=data['account']).count()
        if names >= 1:
            flash("已有此用户，请使用其他用户名！")
            return redirect(url_for("scholar.register"))
        new_user = User(
            id=None,
            username=data['account'],
            password=data['pwd']
        )
        db.session.add(new_user)
        db.session.commit()
        flash("注册成功！")
        return redirect(url_for("scholar.login"))
    return render_template("login/register.html", form=form)


# 验证码路由
@scholar_blue.route('/code/')
def code():
    """生成验证码图片流"""
    image, code = get_verify_code()
    buf = BytesIO()
    image.save(buf, 'jpeg')
    buf_str = buf.getvalue()
    response = make_response(buf_str)
    response.headers['Content-Type'] = 'image/gif'
    session['image'] = code
    return response


@scholar_blue.route("/search", methods=["GET", "POST"])
@scholar_log_req
def search():
    form = SearchForm()
    if form.validate_on_submit():
        data = form.data
        print("searchData", data)
        if data['searchInput'] is not None:
            return redirect(url_for("scholar.entities", keyword=data['searchInput'], page=1))
        # query['query']['query_string']['query'] = data['searchInput']
        # print(query)
        # result = es.search(index='scholar', doc_type='teacherInfo', body=query)
        # print(result)
    return render_template("search/search.html", form=form)


@scholar_blue.route("/entities/<string:keyword>&<int:page>", methods=["GET", "POST"])
@scholar_log_req
def entities(keyword, page=1):
    page_size = 3
    # print("page", page)
    query = {
        "query": {
            "query_string": {
                "default_field": "paper",
                "query": keyword
            }
        },
        "from": page - 1,
        "size": page_size
    }
    result = es.search(index='scholar', doc_type='teacherInfo', body=query)
    total = result['hits']['total']
    rest = total % page_size
    # print("rest", rest)
    res_dict = result['hits']['hits']
    page_num = ceil(total / page_size)
    # print("page_num", page_num)
    if page == page_num:
        res_dict = res_dict[-rest:]
    # print(res_dict)
    return render_template("search/entities.html", kw=keyword, search_items=res_dict, page=page, page_num=page_num)


@scholar_blue.route("/favor", methods=["GET", "POST"])
@scholar_log_req
def favor():
    return render_template("search/favor.html")


@scholar_blue.route("/professor/<string:name>", methods=["GET", "POST"])
@scholar_log_req
def professor(name):
    # 这个地方需要传入被点击的实验者的姓名, 然后在数据库中进行搜索展示
    researcher = Researcher.query.filter_by(Name=name).first()
    if researcher.DOB == "":
        researcher.DOB = "Unknown"
    Researcher_info = {"ID": researcher.ID, "Name": researcher.Name, "Avatar": researcher.Avatar,
                        "Title": researcher.Title, "HomePage": researcher.HomePage, "University": researcher.University,
                        "Lab": researcher.Lab, "Bio": researcher.Bio, "Sig": researcher.Signature,
                        "DOB": researcher.DOB, "Email": researcher.Email,
                        "Mottos": json.loads(researcher.Mottos)["Mottos"],
                        "ResearchInterest": json.loads(researcher.ResearchInterest)["ResearchInterest"],
                        "Awards": json.loads(researcher.Awards)["Awards"],
                        "Co_authors": json.loads(researcher.Co_authors)["Co_authors"],
                        "Papers": json.loads(researcher.Papers)["Papers"],
                        "Cited_graph": json.loads(researcher.Cited_graph)["Cited_graph"],
                    }
    print("Researcher_info[Awards]", Researcher_info["Awards"])
    return render_template("search/professor.html", Researcher_info=Researcher_info)


@scholar_blue.route("/paper/<string:name>", methods=["GET", "POST"])
@scholar_log_req
def paper(name):
    # 这个地方需要传入被点击的实验者的姓名, 然后在数据库中进行搜索展示
    researcher = Researcher.query.filter_by(Name=name).first()
    if researcher.DOB == "":
        researcher.DOB = "Unknown"
    researcher_info = {"ID": researcher.ID, "Name": researcher.Name, "Avatar": researcher.Avatar,
                        "Title": researcher.Title, "HomePage": researcher.HomePage, "University": researcher.University,
                        "Lab": researcher.Lab, "Bio": researcher.Bio, "Sig": researcher.Signature,
                        "DOB": researcher.DOB, "Email": researcher.Email,
                        "Mottos": json.loads(researcher.Mottos)["Mottos"],
                        "ResearchInterest": json.loads(researcher.ResearchInterest)["ResearchInterest"],
                        "Awards": json.loads(researcher.Awards)["Awards"],
                        "Co_authors": json.loads(researcher.Co_authors)["Co_authors"],
                        "Papers": json.loads(researcher.Papers)["Papers"],
                        "Cited_graph": json.loads(researcher.Cited_graph)["Cited_graph"],
                    }
    print("Researcher_info[Papers]", researcher_info["Papers"])
    return render_template("search/paper.html", Researcher_info=researcher_info)


@scholar_blue.route("/connection:<string:name>", methods=["GET", "POST"])
@scholar_log_req
def connection(name):
    # 这个地方需要传入被点击的实验者的姓名, 然后在数据库中进行搜索展示
    researcher = Researcher.query.filter_by(Name=name).first()
    if researcher.DOB == "":
        researcher.DOB = "Unknown"
    researcher_info = {"ID": researcher.ID, "Name": researcher.Name, "Avatar": researcher.Avatar,
                        "Title": researcher.Title, "HomePage": researcher.HomePage, "University": researcher.University,
                        "Lab": researcher.Lab, "Bio": researcher.Bio, "Sig": researcher.Signature,
                        "DOB": researcher.DOB, "Email": researcher.Email,
                        "Mottos": json.loads(researcher.Mottos)["Mottos"],
                        "ResearchInterest": json.loads(researcher.ResearchInterest)["ResearchInterest"],
                        "Awards": json.loads(researcher.Awards)["Awards"],
                        "Co_authors": json.loads(researcher.Co_authors)["Co_authors"],
                        "Papers": json.loads(researcher.Papers)["Papers"],
                        "Cited_graph": json.loads(researcher.Cited_graph)["Cited_graph"],
                    }
    print("Researcher_info[Papers]", researcher_info["Papers"])
    return render_template("search/connection.html", Researcher_info=researcher_info)


@scholar_blue.route("/operateFavor", methods=["POST"])
def oprateFavor():
    json_data = request.get_json()
    print(json_data["id"], json_data["op"])
    return jsonify(res="success", id=json_data["id"], op=json_data["op"])
