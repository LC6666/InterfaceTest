# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import json

# fp = open("../case/case.json")
# data = json.load(fp)
# print(data['user1'])
# fp.close()


class OperationJson:
    def __init__(self):
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open("../case/case.json") as fp:
            data = json.load(fp)
            return data

    def get_data(self,key):
        return self.data[key]




if __name__ == '__main__':
    jsondata = OperationJson()
    jsondata.get_data('user1')