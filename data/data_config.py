# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

class global_var:
    #编号
    Id = '0'
    # 模块
    module = '1'
    # 用例名称
    casename='2'
    # 用例描述
    casedescribe='3'
    # 前置条件
    casecondition='4'
    # 请求URI
    caseurl = '5'
    # 请求方法
    casemethod= '6'
    # 请求头
    caseheader = '7'
    # 发送数据
    casedata = '8'
    # 返回状态码
    caserecode = '9'
    # 期望结果
    caseresult = '10'
    # 是否执行
    execute = '11'



    def get_caseid(self):
        return global_var.Id
    def get_module(self):
        return global_var.module
    def get_casename(self):
        return global_var.casename
    def get_casedescribe(self):
        return global_var.casedescribe
    def get_casecondition(self):
        return global_var.casecondition
    def get_caseurl(self):
        return global_var.caseurl
    def get_casemethod(self):
        return global_var.casemethod
    def get_caseheader(self):
        return global_var.caseheader
    def get_casedata(self):
        return global_var.casedata
    def get_caserecode(self):
        return global_var.caserecode
    def get_caseresult(self):
        return global_var.caseresult
    def get_execute(self):
        return global_var.execute
