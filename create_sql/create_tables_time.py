#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from config import mysql_val, tables4

def create_table():
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    for i in tables4:
        print i
        # 如果数据表已经存在使用execute()方法删除表
        cursor.execute("DROP TABLE IF EXISTS %s"% (i))
        # 创建数据表SQL语句
        sql = """CREATE TABLE `%s` (
          `id` int(10) NOT NULL AUTO_INCREMENT,
          `TaskId` int(10) NOT NULL,
          `Times` date default NULL,
          `%s` time default NULL,
          `DNSTime` float(10) NOT NULL,
          `EstablishConnectionTime` float(10) NOT NULL,
          `SSLHandshakeTime` float(10) NOT NULL,
          `FirstPackageTime` float(10) NOT NULL,
          `ClientTime` float(10) NOT NULL,
          `ContentDownloadTime` float(10) NOT NULL,
          `TotalDownloadTime` float(10) NOT NULL,
          `FirstScreenTime` float(10) NOT NULL,
          `MonitoringPoints` int(10) NOT NULL,
          `ErrorPoints` int(10) NOT NULL,
          `Usability` float(40) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % (i, i.capitalize())
        # 执行SQL语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    # 关闭数据库连接
    db.close()

print "Created table Successfull."

# 初始化或者调用函数
if __name__ == "__main__":
    create_table()