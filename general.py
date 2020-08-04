#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from tingyun_data import get_data
from config import request_val, mysql_val, times

def data_insert(data):
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    result = []
    for j in data['list']['NBChart'][0]['chart-data']['serieses']['series'][0]['rows']['row']:
        j = j['cols']['col']
        result.append(j)

    for k in range(len(result)):
        result1 = []
        for l in result[k]:
            l = l['value']
            result1.append(l)
        result2 = [request_val['taskId'], times] + result1
        print result2

        insert = "insert into general(TaskId,Times,DNSTime,EstablishConnectionTime,SSLHandshakeTime,FirstPackageTime," \
                 "ClientTime,ContentDownloadTime,TotalDownloadTime,FirstScreenTime,MonitoringPoints,ErrorPoints," \
                 "Usability)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # 执行SQL语句
        cursor.execute(insert, result2)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()

    print "Created table Successfull."

# 初始化或者调用函数
if __name__ == "__main__":
    chartId = 'componentsByTask'
    data = get_data(chartId)
    data_insert(data)