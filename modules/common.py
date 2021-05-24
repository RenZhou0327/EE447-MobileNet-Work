from functools import wraps
from flask import session, redirect, url_for, request, flash
from elasticsearch import Elasticsearch

def scholar_log_req(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        print(f)
        print(session)
        if 'admin' not in session:
            flash("您尚未登录！")
            return redirect(url_for("scholar.login", next=request.url))
        return f(*args, **kwargs)

    return decorated_function


graph_list = [(0, 1), (0, 2), (0, 3)]
# es = Elasticsearch("172.17.0.7:9200")
# es = Elasticsearch("1.15.106.125:9200")
# ES_HOST = {
#             "host": "localhost",
#             "port": 9205
#         }
es = Elasticsearch()
