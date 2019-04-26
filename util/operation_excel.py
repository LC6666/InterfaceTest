# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import xlrd

data = xlrd.open_workbook('../case/case.xlsx')
tables = data.sheet_by_index(0)
print(tables.nrows)
print(tables.cell(0,3))

