from django.test import TestCase
import requests
import json

# Create your tests here.

class RunMain:

    def __init__(self,url,method,data=None):
        self.res = self.run_main(url,method,data)


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


if __name__ == '__main__':
    url = 'http://127.0.0.1:8000/login/'
    data = {
        'username': 'LC001',
        'password': '21218cca77804d2ba1922c33e0151105',
        'validate': 'wxym3'}
    run = RunMain(url,'POST',data)
    print(run.res)
    url2 = 'http://127.0.0.1:8000/login/?username=LC001&password=21218cca77804d2ba1922c33e0151105'
    run2 = RunMain(url2, 'GET')
    print(run2.res)


