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
    hoperesult = '10'
    # 实际结果
    caseresult = '11'
    # 是否执行
    execute = '12'



def get_caseid():    
    return global_var.Id    
def get_module():    
    return global_var.module    
def get_casename():    
    return global_var.casename    
def get_casedescribe():    
    return global_var.casedescribe    
def get_casecondition():    
    return global_var.casecondition    
def get_caseurl():    
    return global_var.caseurl    
def get_casemethod():    
    return global_var.casemethod    
def get_caseheader():    
    return global_var.caseheader    
def get_casedata():    
    return global_var.casedata    
def get_caserecode():    
    return global_var.caserecode    
def get_hoperesult():
    return global_var.hoperesult
def get_caseresult():
    return global_var.caseresult
def get_execute():    
    return global_var.execute    
