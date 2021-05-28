from functools import wraps
from flask import session, redirect, url_for, request, flash
from elasticsearch import Elasticsearch
from app import db
from modules.scholar.models import Researcher, SimTable
from  sqlalchemy.sql.expression import func
import random


def scholar_log_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            flash("您尚未登录！")
            return redirect(url_for("scholar.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def get_recomm_professor(t_name_list):
    recomm_list = db.session.query(SimTable.dst).filter(SimTable.src.in_(t_name_list)).limit(30).all()
    recomm_list = [prof[0] for prof in recomm_list]
    print("recomm", recomm_list)
    if len(recomm_list) == 0:
        recomm_professors = db.session.query(Researcher.Name, Researcher.Avatar, Researcher.University,
                                             Researcher.Title).order_by(func.rand()).limit(20).all()
        print("here")
    else:
        recomm_professors = db.session.query(Researcher.Name, Researcher.Avatar, Researcher.University,
                                         Researcher.Title).filter(Researcher.Name.in_(recomm_list)).all()
    random.shuffle(recomm_professors)
    print(recomm_professors)
    if len(recomm_professors) <= 10:
        return recomm_professors
    return recomm_professors[:10]

# def get_professor_by_id(id_list):
#     recomm_professor_list = db.session.query(Researcher.Name, Researcher.Avatar, Researcher.University,
#                                              Researcher.Title).filter(Researcher.ID.in_(id_list)).all()
#     print(recomm_professor_list)
#     return recomm_professor_list
#
#
# def random_walk_recomm_list(pid_list):
#     print("random_walk_recomm_list", pid_list)
#     return [0, 1, 2]
#
#
# def random_walk_recomm_int(pid):
#     print("random_walk_recomm_int", pid)
#     return [1, 2]


graph_list = [(0, 1), (0, 2), (0, 3)]
# es = Elasticsearch("172.17.0.7:9200")
# es = Elasticsearch("1.15.106.125:9200")
# ES_HOST = {
#             "host": "localhost",
#             "port": 9205
#         }
es = Elasticsearch()
