# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import json

# fp = open("../case/case.json")
# data = json.load(fp)
# print(data['user1'])
# fp.close()


class OperationJson:
    def __init__(self,file_path=None):
        if file_path == None:
            self.file_path='../case/case.json'
        else:
            self.file_path = file_path
        self.data = self.read_data()

    # 读取json文件
    def read_data(self):
        with open(self.file_path) as fp:
            data = json.load(fp)
            return data

    #根据关键字获取数据
    def get_data(self,key):
        return self.data[key]

    #写json
    def write_data(self,data):
        with open("../case/cookie.json",'w') as fp:
            fp.write(json.dumps(data))



if __name__ == '__main__':
    jsondata = OperationJson()
    print((jsondata.get_data('user1')))