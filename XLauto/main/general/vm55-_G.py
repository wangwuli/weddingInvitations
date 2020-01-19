# -*- coding: utf-8 -*-
#!/usr/bin/env python
#
# Written by wuli.wang
# take example by: https://www.jianshu.com/p/843782e454a8 , https://www.jianshu.com/p/2242b9920960 , https://www.jianshu.com/p/3e4fc8ee9f51


import atexit
from pprint import pprint

from pyvim import connect
from pyVmomi import vim, vmodl

# import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')

class NewVmClass():

    def connect(self,host,user,pwd,port=443):
        """
        连接vCenter Server
        :param host:
        :param user:
        :param pwd:
        :param port:
        :return:
        """
        self.vm_ces = connect.SmartConnectNoSSL(host=host,
                                       user=user,
                                       pwd=pwd,
                                       port=port)

        self.content = self.vm_ces.RetrieveContent()

        return True


    def disconnect(self):
        """
        关闭vCenter Server
        :return:
        """
        atexit.register(connect.Disconnect, self.vm_ces)

        return True


    # 打印虚拟机详情
    def print_vm_info(self,virtual_machine):
        """
        Print information for a particular virtual machine or recurse into a
        folder with depth protection
        """

        dict_return = {}
        summary = virtual_machine.summary
        dict_return['name'] = pprint(summary.config.name)
        dict_return['uuid'] = summary.config.instanceUuid
        if summary.guest is not None:
            ip_address = summary.guest.ipAddress
            if ip_address:
                dict_return['ip'] = ip_address
            else:
                dict_return['ip'] = None
        if summary.runtime.question is not None:
            print("Question  : ", summary.runtime.question.text)

        # file_obj = open("./ZJYYVMtest.txt", "a")
        # file_obj.write(str(dict_return) + '\n')
        # file_obj.close()
        print (dict_return)


    def get_vm_host_info(self):
        # 获取所有虚拟机对象
        container = self.content.rootFolder  # starting point to look into
        viewType = [vim.VirtualMachine]  # object types to look for
        recursive = True  # whether we should look into it recursively
        containerView = self.content.viewManager.CreateContainerView(container, viewType, recursive)

        # 遍历虚拟机列表打印虚拟机详情
        children = containerView.view
        for child in children:
            self.print_vm_info(child)


    def get_me_vm_obj(self,vm_name_one):
        """
        获取虚拟机名称对象
        :param vm_name_one:
        :return:
        """
        objView = self.content.viewManager.CreateContainerView(self.content.rootFolder,
                                                          [vim.VirtualMachine],
                                                          True)
        vmList = objView.view

        for vm in vmList:
            if str(vm.name) == vm_name_one:
                return vm

            if vm.name.find('102.31') != -1:
                pass


        return False


test=NewVmClass()

test.connect(host='192.18.254.10',user='root',pwd='Actech@123')
#test.connect(host='192.168.10.200',user='root',pwd='cbh@qq.com123')

# vm = test.get_me_vm_obj('102.31 建行聚合付A')
# vm.PowerOff()
#vm.PowerOn()

#获取所有虚拟机对象
test.get_vm_host_info()

test.disconnect()