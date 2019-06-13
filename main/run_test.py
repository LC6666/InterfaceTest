# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from tests.runmethod import RunMethod
from data.get_data import GetData
from util.common_util import CommUtil
from data.depend_data import DependData
from util.send_email import SendEmail
from util.operation_header import OperationHeader
from util.operation_json import OperationJson
import json

class RunTest:

    def __init__(self):
        self.run_method = RunMethod()
        self.data = GetData()
        self.commonUtil = CommUtil()
        self.send_mail = SendEmail()

    def go_on_run(self):
        res = None
        pass_count = []
        fail_count = []
        rowcount = self.data.get_case_rowCount()
        for i in range(1,rowcount):

            is_run = self.data.get_is_run(i)

            if is_run:
                url = self.data.get_url(i)
                method = self.data.get_request_method(i)
                data = self.data.get_data_for_json(i)
                is_cookie = self.data.get_cookies(i)
                header = self.data.is_header(i)
                hoperesult = self.data.get_hopereval(i)
                is_depend = self.data.is_depend(i)
                # 是否需要依赖
                if is_depend != None:
                    self.depend_data = DependData(is_depend)
                    # 获取依赖的响应数据
                    depend_response_data = self.depend_data.get_data_for_key(i)
                    # 获取依赖的key
                    depend_key = self.data.get_depend_field(i)
                    data[depend_key] = depend_response_data

                # 是否保存cookies
                if is_cookie =='write':
                    res = self.run_method.run_main(method,url,data)
                    op_headers = OperationHeader(res)
                    op_headers.write_cookie()

                elif is_cookie =='yes':
                    op_json = OperationJson('../case/cookie.json')
                    res = self.run_method.run_main(method,url,data,op_json.data)
                else:
                    res = self.run_method.run_main(method,url,data)

                res =res.content.decode('utf-8')
                print(res)

                if self.commonUtil.is_contain(hoperesult,res):
                    self.data.write_realresult(i,res)
                    self.data.write_result(i,"测试成功")
                    pass_count.append(i)

                else:
                    self.data.write_realresult(i, res)
                    self.data.write_result(i, "测试失败")
                    fail_count.append(i)

                res = json.loads(res);
                if (res['statusCode'] != "200"):
                    print(res['errorMsg'])


        # self.send_mail.send_mail_main(pass_count,fail_count)


if __name__ == '__main__':
    run = RunTest()
    res = run.go_on_run()




