# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import requests
from util.operation_json import OperationJson

class OperationHeader:

    def __init__(self,response):
        self.response = response

    def get_response_url(self):
        '''获取登录返回的token的url'''
        url = self.response['data']['url'][0]

    def get_cookie(self):
        '''获取cookie的jar'''
        cookie = ''
        return cookie


    def write_cookie(self):
        cookie = requests.utils.dict_from_cookiejar(self.response.cookies)
        op_json = OperationJson()
        op_json.write_data(cookie)



if __name__ == '__main__':
    url = "http://iebm.scada.com/api/login"
    data = {
        "username": "admin",
        "password": "21218cca77804d2ba1922c33e0151105",
        "validate": "x2"
    }

    res = requests.post(url,data)
    op_headers = OperationHeader(res)
    cookie = op_headers.get_cookie()
    op_headers.write_cookie()

    # url2 = "http://iebm.scada.com/api/menu/userMenus"
    # res2 = requests.get(url2, cookie)
    # print(res2.json())




