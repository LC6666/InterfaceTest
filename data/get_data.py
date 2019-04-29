# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data import data_config

class GetData:

    def __init__(self):
        self.case_excel = OperationExcel('../case/case2.xlsx','Sheet1')

    def get_case_rowCount(self):
        return self.case_excel.get_rowCount()

    def get_case_id(self,rowx):
        colx = data_config.get_caseid()
        return self.case_excel.get_cellVale(rowx,colx)



    # 是否执行用例
    def get_is_run(self,rowx):
        flag = None
        colx = data_config.get_execute()
        run_model = self.case_excel.get_cellVale(rowx,colx)
        if run_model=='yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否有header
    def is_header(self,rowx):
        colx = data_config.get_caseheader()
        header = self.case_excel.get_cellVale(rowx, colx)
        if header != None and header!='':
            return header

    # 获取请求方式
    def get_request_method(self,rowx):
        colx = data_config.get_casemethod()
        request_method = self.case_excel.get_cellVale(rowx,colx)
        return request_method

    # 获取请求url
    def get_url(self,rowx):
        colx = data_config.get_caseurl()
        url = self.case_excel.get_cellVale(rowx,colx)
        return url

    # 请求数据
    def get_request_data(self,rowx):
        colx = data_config.get_casedata()
        data = self.case_excel.get_cellVale(rowx,colx)
        if data == '':
            return None
        else:
            return data

    # 获取请求数据
    def get_data_for_json(self,rowx):
        key = self.get_request_data(rowx)
        data_json = OperationJson().get_data(key)
        return data_json

    # 获取预期返回值
    def get_hopereval(self,rowx):
        colx = data_config.get_hoperesult()
        return self.case_excel.get_cellVale(rowx,colx)

    # 写入实际返回值
    def write_realresult(self,rowx,value):
        colx = data_config.get_caseresult();
        self.case_excel.write_value(rowx, colx, value)

    # 写入结果记录
    def write_result(self,rowx,value):
        colx = data_config.get_result()
        self.case_excel.write_value(rowx,colx,value)



    # 是否有数据依赖，获取依赖caseid
    def is_depend(self,rowx):
        colx = data_config.get_casedepend()
        depend_case_id = self.case_excel.get_cellVale(rowx,colx)
        if depend_case_id =="":
            return None
        else:
            return depend_case_id

    # 获取数据依赖字段
    def get_depend_field(self,rowx):
        colx =  data_config.get_datadepend()
        return self.case_excel.get_cellVale(rowx,colx)

    # 获取依赖数据的key
    def get_depend_key(self, rowx):
        colx = data_config.get_returndepend()
        depent_key = self.case_excel.get_cellVale(rowx, colx)
        if depent_key == "":
            return None
        else:
            return depent_key
