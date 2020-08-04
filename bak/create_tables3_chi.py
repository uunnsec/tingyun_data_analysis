#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from config import mysql_val, tables3

def data_insert():
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    for i in tables3:
        print i
        # 如果数据表已经存在使用execute()方法删除表
        cursor.execute("DROP TABLE IF EXISTS %s" % i)
        # 创建数据表SQL语句
        sql = """CREATE TABLE `%s` (
          `id` int(10) NOT NULL AUTO_INCREMENT,
          `TaskId` int(10) NOT NULL,
          `时间` varchar(40) NOT NULL,
          `页面序号` int(10) NOT NULL,
          `省份` varchar(40) NOT NULL,
          `城市` varchar(40) NOT NULL,
          `运营商` varchar(40) NOT NULL,
          `接入方式` varchar(40) NOT NULL,
          `操作系统版本` varchar(40) NOT NULL,
          `浏览器版本` varchar(40) NOT NULL,
          `flash版本` varchar(40) NOT NULL,
          `DNS服务器` varchar(40) NOT NULL,
          `监测点IP` varchar(40) NOT NULL,
          `主机IP` varchar(40) NOT NULL,
          `主机城市` varchar(40) NOT NULL,
          `主机运营商` varchar(40) NOT NULL,
          `错误描述` varchar(40) NOT NULL,
          `总下载时间` float(40) NOT NULL,
          `总下载字节数` float(40) NOT NULL,
          `下载速度` float(40) NOT NULL,
          `首屏时间` float(40) NOT NULL,
          `DNS时间` float(40) NOT NULL,
          `建立连接时间` float(40) NOT NULL,
          `SSL握手时间` float(40) NOT NULL,
          `重定向时间` float(40) NOT NULL,
          `发出请求时间` float(40) NOT NULL,
          `首包时间` float(40) NOT NULL,
          `内容下载时间` float(40) NOT NULL,
          `关闭连接时间` float(40) NOT NULL,
          `客户端时间` float(40) NOT NULL,
          `网络层时间` float(40) NOT NULL,
          `基础页面下载时间` float(40) NOT NULL,
          `基础页面下载字节数` float(40) NOT NULL,
          `基础页面下载速度` float(40) NOT NULL,
          `首屏对象数` float(40) NOT NULL,
          `首屏下载字节数` float(40) NOT NULL,
          `DNS解析次数` float(40) NOT NULL,
          `DNS解析总时间` float(40) NOT NULL,
          `建立连接次数` float(40) NOT NULL,
          `建立连接总时间` float(40) NOT NULL,
          `页面对象数` float(40) NOT NULL,
          `DOM元素个数` float(40) NOT NULL,
          `IFRAME个数` float(40) NOT NULL,
          `接收额外数据时间` float(40) NOT NULL,
          `页面打开时间` float(40) NOT NULL,
          `元素错误量` float(40) NOT NULL,
          `脚本错误` varchar(40) NOT NULL,
          `HTTPServer` varchar(40) NOT NULL,
          `HTTPVia` varchar(40) NOT NULL,
          `无Compress头元素个数` float(40) NOT NULL,
          `无Expires头元素个数` float(40) NOT NULL,
          `无Etag头元素个数` float(40) NOT NULL,
          `平均CPU使用率` float(40) NOT NULL,
          `当前任务CPU使用率` float(40) NOT NULL,
          `平均内存使用率` float(40) NOT NULL,
          `当前任务内存使用率` float(40) NOT NULL,
          `平均下载速度` float(40) NOT NULL,
          `首次渲染时间` float(40) NOT NULL,
          `自定义渲染时间` float(40) NOT NULL,
          `DOM处理结束时间` float(40) NOT NULL,
          `onLoad事件开始时间` float(40) NOT NULL,
          `onLoad事件结束时间` float(40) NOT NULL,
          `HTML源码` varchar(40) NOT NULL,
          PRIMARY KEY (`id`)
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8;""" % (i)
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