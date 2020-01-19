# -*- coding: utf-8 -*-
'''
@author: liww liww@cenboomh.com
@file: date_G.py
@time: 2020/1/9 15:40
@desc:
'''

class Datadis():

    def set_strdate(self, strstring):
        """
        读取字符串时间
        :param strstring: 2020-1-9 or 2020:1:9 or 20200109
        :return:
        """
        date_list = []
        strstring = str(strstring)
        if strstring.find('-'):
            date_list = strstring.split('-')
        elif strstring.find(':'):
            date_list = strstring.split(':')
        else:
            date_list[0], date_list[1], date_list[2] = strstring[:4], strstring[4:6], strstring[6:]

        self.year, self.month, self.day = date_list[0], date_list[1], date_list[2]

    #def get_week_day(date):



