from . import services
import os
from flask import request

@services.route('/save_blibli', methods=['GET', 'POST'])
def save_blibli():
    blibli = request.args.get('blibli')
    try:
        os.makedirs("./tmp/")
    except FileExistsError:
        pass
    hooks = open('./tmp/data.txt', 'a')
    hooks.write("%swangwuli" %blibli)
    hooks.close()
    return "保存成功"

@services.route('/get_blibli', methods=['GET', 'POST'])
def get_blibli():
    try:
        os.makedirs("./tmp/")
    except FileExistsError:
        pass
    return_list = []
    hooks = open('./tmp/data.txt', 'r')
    read_text = hooks.read(4096)
    hooks.close()
    read_list = read_text.split("wangwuli")
    #read_list[-1] = read_list[-1] + '...'
    

    return str(read_list[-20:])
