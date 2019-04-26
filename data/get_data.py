# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from util.operation_excel import OperationExcel
from util.operation_json import OperationJson
from data.data_config import global_var

class GetData:

    def __init__(self):
        self.case_excel = OperationExcel('../case/case.xlsx')

    def get_case_lines(self):
        self.case_excel.get_rowNum()

    def get_case_id(self,rowx):
        id=None
        colx = global_var.get_caseid()
        return self.case_excel.get_cellVale(rowx,colx)



    # 是否执行用例
    def get_is_run(self,rowx):
        flag = None
        colx = global_var.get_execute()
        run_model = self.case_excel.get_cellVale(rowx,colx)
        if run_model=='yes':
            flag = True
        else:
            flag = False
        return flag

    # 是否有header
    def is_header(self,rowx):
        colx = global_var.get_caseheader()
        header = self.case_excel.get_cellVale(rowx, colx)
        if header != None & header!='':
            return header

    # 获取请求方式
    def get_request_method(self,rowx):
        colx = global_var.get_casemethod()
        request_method = self.case_excel.get_cellVale(rowx,colx)
        return request_method

    # 获取请求url
    def get_url(self,rowx):
        colx = global_var.get_caseurl()
        url = self.case_excel.get_cellVale(rowx,colx)
        return url


    def get_request_data(self,rowx):
        colx = global_var.get_casedata()
        data = self.case_excel.get_cellVale(rowx,colx)
        if data == '':
            return None
        else:
            return data

    def get_data_for_json(self,rowx):
        data_json = OperationJson.get_data(self.get_case_id(rowx))
        return data_json