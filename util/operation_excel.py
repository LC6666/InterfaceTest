# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import xlrd

data = xlrd.open_workbook('../case/case.xlsx')
tables = data.sheet_by_index(0)
print(tables.nrows)
print(tables.cell(0,3))


class OperationExcel:
    def __init__(self,file_name=None,sheet_name=None):
        if file_name:
            self.file_name = file_name
            self.sheet_name = sheet_name

        else:
            self.file_name='../case/AutoLink_api_tests.xlsx'
            self.sheet_name='Sheet1'
        self.data = self.get_data()

    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_name(self.sheet_name)
        return tables

    def get_rowNum(self):
        tables = self.data
        return tables.nrows

    def get_cellVale(self,rowx,clox):
        return self.data.cell(rowx,clox)

if __name__ == '__main__':
    openers = OperationExcel()
    print(openers.get_rowNum())