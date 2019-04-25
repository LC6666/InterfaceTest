# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import unittest
import json
from .request_test import RunMain

class TestMethod(unittest.TestCase):


    def test_01(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC001',
            'password': '21218cca77804d2ba1922c33e0151105',
            'validate': 'wxym3'}
        res = self.run.run_main(url,'POST',data)
        res = json.loads(res)
        self.assertEqual(res['username'], 'LC002')

    def test_02(self):
        url = 'http://127.0.0.1:8000/login/'
        data = {
            'username': 'LC002',
            'password': 'licheng',
            'validate': 'wxym3'}
        res = self.run.run_main(url, 'POST', data)
        res = json.loads(res)
        self.assertEqual(res['username'],'LC002')

    def setUp(self):
        self.run = RunMain()

if __name__ == '__main__':
    unittest.main()