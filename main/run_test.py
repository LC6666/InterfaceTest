# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"
from tests.runmethod import RunMethod
from data.get_data import GetData

class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()

    def go_on_run(self):
        res = None
        rowcount = self.data.get_case_rowNum()
        for i in (1,rowcount):
            url = self.data.get_url(i)
            method = self.data.get_request_method(i)
            is_run = self.data.get_is_run(i)
            data = self.data.get_data_for_json(i)
            header = self.data.is_header(i)
            print(url,method,is_run,data,header)
            if is_run:
                res = self.run_method.run_main(method,url,data,header)
            return res


if __name__ == '__main__':
    run = RunTest()
    res = run.go_on_run()
    print(res)




