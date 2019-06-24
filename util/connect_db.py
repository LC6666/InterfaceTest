# -*- coding:utf-8 -*-
__author__ = "豆豆嗯嗯"

import MySQLdb.cursors
import json
class OpenrationMysql:
    def __init__(self):
        self.conn = MySQLdb.Connect(
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root',
            db='ssm_yb_test',
            charset='utf8',
            cursorclass=MySQLdb.cursors.DictCursor
        )

        self.cur = self.conn.cursor()

    def search_one(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchone()
        result = json.dumps(result)
        return result

    def seach_all(self,sql):
        self.cur.execute(sql)
        result = self.cur.fetchall()
        result = json.dumps(result)
        return result

if __name__ == '__main__':
    op_mysql = OpenrationMysql()
    result = op_mysql.seach_all("select * from login_test")
    print(result)