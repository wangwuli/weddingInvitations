# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: nmap.py
@time: 2019/12/11 14:55
@desc:
'''
from . import independent


@independent.route('/independent/nmap',methods=['GET','POST','PUT','DELETE'])
def soft_install():
    return "test"