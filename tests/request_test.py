# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from django.test import TestCase
import requests
import json

# Create your tests here.

class RunMain:


    def run_main(self,url,method,data=None):
        res = None
        if method=='GET':
            res = self.send_get(url,data)
        else:
            res = self.send_post(url,data)
        return res


    def send_get(self,url,data):
        res = requests.get(url=url,data=data).json()
        return json.dumps(res,indent=2,sort_keys=True)

    def send_post(self,url, data):
        res = requests.post(url=url, data=data).json()
        # print(res)
        return json.dumps(res,indent=2,sort_keys=True)


