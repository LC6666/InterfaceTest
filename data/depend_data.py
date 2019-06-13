# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"


from util.operation_excel import OperationExcel
from tests.runmethod import RunMethod
from data.get_data import GetData
from main.run_test import RunTest
import json

from jsonpath_rw import jsonpath,parse

class DependData:

    def __init__(self,caseid):
        self.opera_excel = OperationExcel('../case/case2.xlsx','Sheet1')
        self.caseid = caseid
        self.data = GetData()

    # 通过casid获取整行数据
    def get_case_row_data(self):
        return self.opera_excel.get_rowbycaseid(self.caseid)


    # 执行依赖测试，获取结果
    def run_dependent(self):
        run_method = RunMethod()
        row = self.opera_excel.get_rowNumbycaseid(self.caseid)
        request_data = self.data.get_data_for_json(row)
        '''
        只执行依赖用例
        header = self.data.is_header(row)
        method = self.data.get_request_method(row)
        # data = self.data.get_request_data(row)
        url = self.data.get_url(row)
        # res = run_method.run_main(method,url,request_data,header)
        res = run_method.run_main(method, url, request_data)
        '''

        url = self.data.get_url(row)
        method = self.data.get_request_method(row)
        data = self.data.get_data_for_json(row)
        is_cookie = self.data.get_cookies(row)
        header = self.data.is_header(row)
        hoperesult = self.data.get_hopereval(row)
        is_depend = self.data.is_depend(row)
        # 获取依赖的响应数据
        depend_response_data = self.depend_data.get_data_for_keys(row)
        # 获取依赖的key
        depend_key = self.data.get_depend_field(row)
        run = RunTest()
        res = run.run_testcase(url, method, data, is_cookie, header, hoperesult, is_depend, depend_response_data, depend_key)

        return json.loads(res.content)

    # 根据依赖的key去获取依赖测试case的响应，然后返回数据依赖字段的值
    def get_data_for_key(self,rowx):
        # 获取数据依赖字段的key
        depend_data = self.data.get_depend_key(rowx)
        # 执行依赖测试，获取数据依赖测试返回值
        res = self.run_dependent()
        # 通过key获取依赖测试的值
        json_exe = parse(depend_data)
        madle = json_exe.find(res)
        return [math.value for math in madle][0]

        # 根据依赖的key去获取依赖测试case的响应，然后返回数据依赖字段的值
    def get_data_for_keys(self, rowx):
        # 获取数据依赖字段的key
        depend_datas = self.data.get_depend_key(rowx)
        # 执行依赖测试，获取数据依赖测试返回值
        res = self.run_dependent()

        reval = {}
        for depend_data in (depend_datas.split(",")):
            # 通过key获取依赖测试的值
            json_exe = parse(depend_data)
            madle = json_exe.find(res)
            for m in madle:
                print(m)
                reval[depend_data] = m
        # print(reval)
        return reval


if __name__ == '__main__':
    data = '{"status":true,"statusCode":"200","errorMsg":"\u8bf7\u6c42\u6210\u529f","data":{"id": 1,"code":"admin","orgId":1,"name":"admin","type":"sysuser","createUser":"admin","createTime":1529654754000,"updateUser":"sysuser","updateTime":1529658285000,"enable":1,"deleteFlag":0,"password":"","nickName":"\u8d85\u7ea7\u7ba1\u7406\u5458","phone":"13113113111","remark":"asaa"}}'
    res = "errorMsg"
    json_exe = parse(res)
    madle = json_exe.find(json.loads(data))
    for m in madle:
        print(m.value)


