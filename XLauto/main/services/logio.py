# -*- coding: utf-8 -*-
'''
@author: liww
@file: logio.py
@time: 2019/11/22 17:10
@desc:
'''

from . import services
from flask import current_app

@services.route('/login')
def login():
    return "test"