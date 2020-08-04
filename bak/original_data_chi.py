#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from tingyun_data import get_data1
from config import request_val1, mysql_val

def data_insert(data):
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()

    data = data.split('\r\n')
    num = len(data)
    for k in data:
        if k == '':
            data.remove(k)
    for i in data[1:num]:
        data = i.split('",')
        result = []
        for j in data:
            result.append(j.strip('"'))
        result1 = [request_val1['taskId']] + result

        print len(result1)

        insert = "insert into original_data(TaskId,时间,页面序号,省份,城市,运营商,接入方式,操作系统版本,浏览器版本,flash版本," \
                 "DNS服务器,监测点IP,主机IP,主机城市,主机运营商,错误描述,总下载时间,总下载字节数,下载速度,首屏时间,DNS时间," \
                 "建立连接时间,SSL握手时间,重定向时间,发出请求时间,首包时间,内容下载时间,关闭连接时间,客户端时间,网络层时间," \
                 "基础页面下载时间,基础页面下载字节数,基础页面下载速度,首屏对象数,首屏下载字节数,DNS解析次数,DNS解析总时间," \
                 "建立连接次数,建立连接总时间,页面对象数,DOM元素个数,IFRAME个数,接收额外数据时间,页面打开时间,元素错误量," \
                 "脚本错误,HTTPServer,HTTPVia,无Compress头元素个数,无Expires头元素个数,无Etag头元素个数,平均CPU使用率," \
                 "当前任务CPU使用率,平均内存使用率,当前任务内存使用率,平均下载速度,首次渲染时间,自定义渲染时间,DOM处理结束时间," \
                 "onLoad事件开始时间,onLoad事件结束时间,HTML源码)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert = "update operator set DNSTime=%s"%result1
        cursor.execute(insert, result1)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()

    print "Created table Successfull."

# 初始化或者调用函数
if __name__ == "__main__":
    data = get_data1()
    data_insert(data)