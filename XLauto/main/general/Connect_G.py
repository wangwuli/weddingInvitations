# -*- coding: utf-8 -*-
'''
@author: liww
@file: Connect_G.py
@time: 2019/12/5 17:02
@desc:
'''
import os
import shlex
import subprocess
import paramiko


class SSHMet():
    def __init__(self):
        self.ip = None
        self.username = None
        self.password = None
        self.port = None
        self.timeout = 30

    def connect(self):
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.user, self.pwd, timeout=self.timeout, banner_timeout=10)
        return self.ssh

    def execcmd(self, cmd):
        """/
        执行单条命令
        :param cmd:
        :return:
        """
        # env = 'source .bash_profile;source /etc/profile;export LANG=en_US.UTF-8;'
        # stdin, stdout, stderr = self.ssh.exec_command('%s%s' % (env, cmd))
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        result = ''.join(stdout.read() + stderr.read()).strip()
        return result

    def execrealtime(self, shell_cmd, object_):
        """
        实时获取命令执行结果
        :param shell_cmd:
        :param object_: 实时接收处理消息的方法
        :return:
        """
        cmd = shlex.split(shell_cmd)
        p = subprocess.Popen(cmd, stdout=subprocess.PIPE, bufsize=1)
        for line in iter(p.stdout.readline, b''):
            object_(line)
        p.stdout.close()
        p.wait()

    def close(self):
        self.ssh.close()


class SCPMet(SSHMet):

    def connect(self):
        self.ssh = paramiko.Transport((self.ip,self.port))
        self.connect(username=self.username, password=self.password)
        self.sftp = paramiko.SFTPClient.from_transport(self.ssh)
        return self.sftp

    def get_file(self,src_file,des_file):
        self.sftp.get(src_file,des_file)
        return des_file

    def put_file(self,src_file,des_file):
        self.sftp.put(src_file,des_file)

        # all_files = self.__get_all_files_in_local_dir(local_dir)
        # for x in all_files:
        #     filename = os.path.split(x)[-1]
        #     remote_filename = remote_dir + '/' + filename
        #     print
        #     u'Put文件%s传输中...' % filename
        #     sftp.put(x, remote_filename)

        return des_file

    def list_dir(self,dir_name):
        return self.sftp.listdir(dir_name)

    def __get_all_files_in_local_dir(self, local_dir):
        all_files = list()
        files = os.listdir(local_dir)
        for x in files:
            filename = os.path.join(local_dir, x)
            if os.path.isdir(x):
                all_files.extend(self.__get_all_files_in_local_dir(filename))
            else:
                all_files.append(filename)
        return all_files

