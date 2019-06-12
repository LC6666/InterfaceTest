# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import os,sys
import xlrd
from xlutils3 import copy


class OperationExcel:
    def __init__(self,file_name=None,sheet_name=None):
        if file_name:
            self.file_name = file_name
        if sheet_name:
            self.sheet_name = sheet_name

        else:
            self.file_name='../case/AutoLink_api_tests.xlsx'
            self.sheet_name='Sheet1'

        self.data = self.get_data()

    # 获取表格
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheet_by_name(self.sheet_name)
        return tables


    #获取某一列的内容
    def get_cols_data(self,colsx=None):
        cols = None
        if colsx != None:
            cols = self.data.col_values(colsx)
        else:
            cols = self.data.col_values(0)
        return cols

    # 获取行数
    def get_rowCount(self):
        return self.data.nrows

    # 获取单元格内容
    def get_cellVale(self,rowx,colx):
        return self.data.cell_value(int(rowx),int(colx))


    # 写入数据
    def write_value(self,rowx,colx,value):
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy.copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(int(rowx),int(colx),value)
        write_data.save(self.file_name)

    # 根据caseid获取该行的内容
    def get_rowbycaseid(self,caseid):
        rowNum = self.get_rowNumbycaseid(caseid)
        return self.get_rowBycaseid(rowNum)

    # 根据caseid找到对应的行号
    def get_rowNumbycaseid(self,caseid):
        num = 0
        cols_data = self.get_cols_data()
        for col_data in cols_data:
            if caseid == col_data:
                return num
            num = num+1


    # 根据rowid获取该行的内容
    def get_rowByNum(self,rowx):
        tables = self.data
        row_data = tables.row_values(rowx)
        return row_data




if __name__ == '__main__':
    openers = OperationExcel()
    print(openers.get_rowNum())