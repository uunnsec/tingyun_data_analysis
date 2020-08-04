#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from config import mysql_val

def data_insert():
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    # 如果数据表已经存在使用execute()方法删除表
    cursor.execute("DROP TABLE IF EXISTS taskid")
    # 创建数据表SQL语句
    sql = """CREATE TABLE `taskid` (
      `id` int(10) NOT NULL AUTO_INCREMENT,
      `taskId` int(10) NOT NULL,
      `Host` varchar(40) NOT NULL,
      PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8;"""
    # 执行SQL语句
    cursor.execute(sql)

    result = [[2179557, 'http://www.huanqiu.com'],[2908514, 'https://3w.huanqiu.com']]
    for i in result:
        print i
        insert = "insert into taskid(taskId,Host)values (%s,%s)"
        # insert = "update operator set DNSTime=%s"%result1
        cursor.execute(insert, i)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()

    print "Created table Successfull."

# 初始化或者调用函数
if __name__ == "__main__":

    data_insert()