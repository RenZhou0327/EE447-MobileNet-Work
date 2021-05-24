from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
# from datetime import timedelta

app = Flask(__name__)

# 配置数据库
# 设置连接数据库
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://root:123456@127.0.0.1:3306/scholar?charset=utf8"
# 数据库和模型类同步修改
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True
# 查询时显示原始SQL语句
app.config["SQLALCHEMY_ECHO"] = False
# sql 连接的秒数
app.config["SQLALCHEMY_POOL_RECYCLE"] = 20

# 密钥配置
app.config["SECRET_KEY"] = "d890fbe7e26c4c3eb557b6009e3f4d3d"

# 调试开关，生成环境是关闭的
app.debug = True
# 注册数据模型
db = SQLAlchemy(app)

# 设置网页缓存时间
# app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(seconds=100)

# 邮件配置
app.config['MAIL_SERVER'] = 'smtp.163.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USE_SSL'] = True
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USERNAME'] = ''
app.config['MAIL_PASSWORD'] = ''

mail = Mail(app)


# 注册蓝图
from modules.scholar import scholar_blue as scholar_blueprint
from modules.home import home_blue as home_blueprint
app.register_blueprint(scholar_blueprint, url_prefix="/scholar")
app.register_blueprint(home_blueprint, url_prefix="/")


@app.errorhandler(404)
def page_not_found(error):
    return render_template("error/404.html"), 404

# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    print("http://localhost:8080/")
    app.run(host='127.0.0.1', debug=True, port=8080)
