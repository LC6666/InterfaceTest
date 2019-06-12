# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import sys
sys.path.append("F:/python work/MyDjangos/MyTester")

import unittest
import json
from mock import mock, Mock
from .request_test import RunMain
from .test_mock import mock_test

class TestMethod(unittest.TestCase):


    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC001',
            'password': '21218cca77804d2ba1922c33e0151105',
            'validate': 'wxym3',
        }
        res = self.run.run_main(url,'POST',data)
        res = json.loads(res)
        self.assertEqual(res['username'], 'LC001')

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC002',
            'password': 'licheng',
            'validate': 'wxym3',
        }
        res = self.run.run_main(url, 'POST', data)
        res = json.loads(res)
        self.assertEqual(res['username'],'LC002')

    def test_03(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC003',
            'password': 'licheng',
            'validate': 'wxym3',
        }
        mock_data = mock.Mock(return_value=data)
        self.run.run_main = mock_data
        res = self.run.run_main(url, 'POST', data)
        self.assertEqual(res['username'], 'LC003')

    def test_04(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC003',
            'password': 'licheng',
            'validate': 'wxym3',
        }
        mock_test(self.run.run_main,data,url,'POST',data)


    def setUp(self):
        self.run = RunMain()

if __name__ == '__main__':
    unittest.main()