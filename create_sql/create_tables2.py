#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from config import mysql_val, tables2

def data_insert():
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    for i in tables2:
        print i
        # 如果数据表已经存在使用execute()方法删除表
        cursor.execute("DROP TABLE IF EXISTS %s" % i)
        # 创建数据表SQL语句
        sql = """CREATE TABLE `%s` (
          `id` int(10) NOT NULL AUTO_INCREMENT,
          `TaskId` int(10) NOT NULL,
          `Times` date default NULL,
          `%s` varchar(40) NOT NULL,
          `DNSTime` float(10) NOT NULL,
          `EstablishConnectionTime` float(10) NOT NULL,
          `SSLHandshakeTime` float(10) NOT NULL,
          `RedirectionTime` float(10) NOT NULL,
          `RequestTime` float(10) NOT NULL,
          `FirstPackageTime` float(10) NOT NULL,
          `ClientTime` float(10) NOT NULL,
          `ContentDownloadTime` float(10) NOT NULL,
          `TotalDownloadTime` float(10) NOT NULL,
          `FirstScreenTime` float(10) NOT NULL,
          `BasicPageDownloadTime` float(10) NOT NULL,
          `NetworkLayerTime` float(10) NOT NULL,
          `BasicPageDownloadBytes` float(40) NOT NULL,
          `BasicPageDownloadSpeed` float(40) NOT NULL,
          `TotalDownloadBytes` float(40) NOT NULL,
          `FirstScreenDownloadBytes` float(40) NOT NULL,
          `FirstScreenObjectsNumber` int(10) NOT NULL,
          `MonitoringPoints` int(10) NOT NULL,
          `ErrorPoints` int(10) NOT NULL,
          `Usability` float(40) NOT NULL,
          `PageObjectsNumber` int(10) NOT NULL,
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
    data_insert()