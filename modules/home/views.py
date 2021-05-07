from modules.home import home_blue
from flask import render_template


@home_blue.route("/")
def index():
    return render_template("home/index.html")
