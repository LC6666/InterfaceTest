# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

#判断是否包含字符串
class CommUtil:
    def is_contain(self,str_one,str_two):
        flag = None
        if str_one in str_two:
            flag = True
        else:
            flag = False
        return flag