# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from data.get_data import data_config
from util.operation_excel import OperationExcel
from tests.runmethod import RunMethod
from data.get_data import GetData
from jsonpath_rw import jsonpath,parse

class DependData:

    def __init__(self,caseid):
        self.opera_excel = OperationExcel()
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
        header = self.data.is_header(row)
        method = self.data.get_request_method(row)
        data = self.data.get_request_data(row)
        url = self.data.get_url(row)
        res = run_method.run_main(method,url,data,header)
        print(res)
        return res

    # 根据依赖的key去获取依赖测试case的响应，然后返回
    def get_data_for_key(self,rowx):
        depend_data = self.data.get_depend_key(rowx)
        res = self.run_dependent()
        json_exe = parse(depend_data)
        madle = json_exe.find(res)
        return [math.value for math in madle][0]
