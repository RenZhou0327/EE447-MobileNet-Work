from functools import wraps
from flask import session, redirect, url_for, request, flash
from elasticsearch import Elasticsearch
from app import db
from modules.scholar.models import Researcher


def scholar_log_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'admin' not in session:
            flash("您尚未登录！")
            return redirect(url_for("scholar.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


def get_professor_by_id(id_list):
    # id_list = [0, 1, 2]
    recomm_professor_list = db.session.query(Researcher.Name, Researcher.Avatar, Researcher.University,
                                             Researcher.Title).filter(Researcher.ID.in_(id_list)).limit(20).all()
    print(recomm_professor_list)
    return recomm_professor_list


def random_walk_recomm():
    return []


graph_list = [(0, 1), (0, 2), (0, 3)]
# es = Elasticsearch("172.17.0.7:9200")
# es = Elasticsearch("1.15.106.125:9200")
# ES_HOST = {
#             "host": "localhost",
#             "port": 9205
#         }
es = Elasticsearch()
