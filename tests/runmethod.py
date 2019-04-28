# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import requests
import json
class RunMethod:

    def post_main(self,url,data,header=None):
        res = None
        if header != None:
            res = requests.post(url=url,data=data,headers=header)
        else:
            res = requests.post(url=url,data=data)
        return res.json()

    def get_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        return res.json()


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method=='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        return json.dumps(res,sort_keys=False,indent=2)

if __name__ == '__main__':
    run = RunMethod()
    res = run.run_main('post','http://127.0.0.1:8000/login/','{"username":"xiaoming","password":"xiaomingpass"}',{"Content-Type":"application/x-www-form-urlencoded"})
    print(res)
