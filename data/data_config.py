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
    # case依赖
    casedepend = '8'
    # 依赖返回数据
    returndepend = '9'
    # 数据依赖字段
    datadepend = '10'
    # 发送数据
    casedata = '11'
    # 返回状态码
    caserecode = '12'
    # 期望结果
    hoperesult = '13'
    # 执行结果
    caseresult = '14'
    # 测试结果
    result = '15'
    # 是否执行
    execute = '16'




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
def get_casedepend():
    return  global_var.casedepend
def get_returndepend():
    return global_var.returndepend
def get_datadepend():
    return global_var.datadepend
def get_casedata():    
    return global_var.casedata    
def get_caserecode():    
    return global_var.caserecode    
def get_hoperesult():
    return global_var.hoperesult
def get_caseresult():
    return global_var.caseresult
def get_result():
    return global_var.result
def get_execute():    
    return global_var.execute

