# from .logio import login

# def init_app(app):
#     login.init_app(app)
from flask import Blueprint

independent = Blueprint('independent', __name__)

from main.independent import nmap