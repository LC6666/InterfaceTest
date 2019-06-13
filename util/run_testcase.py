# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from data.depend_data import DependData
from util.operation_header import OperationHeader
from util.operation_json import OperationJson

class RunCase:

    def run_case(self,url ,method ,data ,is_cookie=None ,header=None ,hoperesult=None ,is_depend=None,depend_response_data=None,depend_key=None):
        res = None
        # 是否需要依赖
        if is_depend != None:
            pass
            # self.depend_data = DependData(is_depend)
            # data[depend_key] = depend_response_data

        # 是否保存cookies
        if is_cookie == 'write':
            res = self.run_method.run_main(method, url, data)
            op_headers = OperationHeader(res)
            op_headers.write_cookie()

        elif is_cookie == 'yes':
            op_json = OperationJson('../case/cookie.json')
            res = self.run_method.run_main(method, url, data, op_json.data)
        else:
            res = self.run_method.run_main(method, url, data)

        res = res.content.decode('utf-8')
        return res