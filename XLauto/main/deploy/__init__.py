# from .logio import login

# def init_app(app):
#     login.init_app(app)
from flask import Blueprint

deploy = Blueprint('deploy', __name__)

from main.deploy import soft