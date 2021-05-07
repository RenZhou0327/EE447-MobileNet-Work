from flask import Blueprint

scholar_blue = Blueprint('scholar', __name__)
from . import views
