# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"



import unittest

class TestMethod(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        print('setUpClass')

    @classmethod
    def tearDownClass(cls):
        print('tearDownClass')

    def setUp(self):
        print('setUp')

    def tearDown(self):
        print('tearDown')

    def test_01(self):
        print('test01')

    def test_02(self):
        print('test02')


if __name__ == '__main__':
    unittest.main()