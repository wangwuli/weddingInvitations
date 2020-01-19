# from .logio import login

# def init_app(app):
#     login.init_app(app)
from flask import Blueprint

services = Blueprint('services', __name__)

from main.services import logio
from main.services import save_blibli
