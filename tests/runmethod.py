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
        # return res.json()
        return res

    def get_main(self,url,data,header):
        res = None
        if header != None:
            res = requests.get(url=url, data=data, headers=header)
        else:
            res = requests.get(url=url, data=data)
        # return res.json()
        return res


    def run_main(self,method,url,data=None,header=None):
        res = None
        if method=='post':
            res = self.post_main(url,data,header)
        else:
            res = self.get_main(url,data,header)
        # return json.dumps(res,sort_keys=False,indent=2)
        return res

if __name__ == '__main__':
    run = RunMethod()
    data = {"disId":"12","disName":"血栓性外痔","disCode":"","disCodeAdd":"","areaCode":"","disType":""}
    data = json.dumps(data)
    print(data)
    res = run.run_main('post','http://192.168.29.156:8120/icd10/model/match',data,{"Content-Type":"application/json;charset=UTF-8"})
    print(res)
