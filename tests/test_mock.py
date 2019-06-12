# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

from mock import mock

import sys
sys.path.append("F:/python work/MyDjangos/MyTester")

# 模拟mock封闭
def mock_test(mock_method,request_data,url,method,response_data):
    mock_method = mock.Mock(return_value=response_data)
    res = mock_method(url,method,request_data)
    return res
