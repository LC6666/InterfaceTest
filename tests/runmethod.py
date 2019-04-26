# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import requests
class RunMethod:

    def post_main(self,url,data,header=None):
        print(url,data)
        res = None
        if header != None:
            # res = requests.post(url=url,data=data,headers=header).json()
            res = requests.post(url=url, data=data)
        else:
            res = requests.post(url=url,data=data).json()
        return res

    def get_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header).json()
        else:
            res = requests.get(url=url, data=data).json()
        return res


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method=='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return res

