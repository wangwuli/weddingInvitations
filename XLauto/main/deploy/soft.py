# -*- coding: utf-8 -*-
'''
@author: liww
@file: soft.py
@time: 2019/12/5 10:06
@desc:
'''
from . import deploy

@deploy.route('/deploy/soft_install',methods=['GET','POST','PUT','DELETE'])
def soft_install():

    return "test"


class conf_file_pro:
    def __init__(self):
        self.name = None
        self.gender = None

    def xml_conf(self):
        return self.name

    def cfg_conf(self):
        return self.gender


class docker(conf_file_pro):
    def __init__(self, name):
        print ("docker")

class yum(conf_file_pro):
    def __init__(self, name):
        print ("yum")

class make(conf_file_pro):
    def __init__(self, name):
        print ("make")


class SoftIstall:
    """
    name: 软件名称,
    type: 部署方式,
    othe_parameter:{
        config:{
            configaddr: { 配置文件相对路径 },
            configparameter:{"key":"value",{{ 配置文件参数 }:{ 设置值 }},
            conftype: {  配置文件格式类型（ini、cfg、xml、config..） } },
    }
    """
    def get_soft(self, name, type, othe_parameter):
        if type == 'docker':
            return docker(name)
        elif type == 'make':
            return make(name)
        elif type == 'yum':
            return yum(name)
