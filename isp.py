#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import pymysql
from tingyun_data import get_data
from config import request_val, mysql_val, times

def data_insert(data):
    db = pymysql.connect(**mysql_val)
    cursor = db.cursor()
    result = []
    for i in data['list']['NBChart'][0]['hearder-def']['rows-def']['row']:
        i = i['name']
        result.append(i)

    result1 = []
    for j in data['list']['NBChart'][0]['chart-data']['serieses']['series'][0]['rows']['row']:
        j = j['cols']['col']
        result1.append(j)

    for k in range(len(result1)):
        result2 = result[k:k + 1]
        result3 = []
        for l in result1[k]:
            l = l['value']
            result3.append(l)
        result4 = [request_val['taskId'], times] + result2 + result3
        print result4

        insert = "insert into isp(taskId,times,Isp,DNSTime,EstablishConnectionTime,SSLHandshakeTime,FirstPackageTime," \
                 "ClientTime,ContentDownloadTime,TotalDownloadTime,FirstScreenTime,MonitoringPoints,ErrorPoints," \
                 "Usability)values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        # insert = "update operator set DNSTime=%s"%result1
        cursor.execute(insert, result4)
    # 提交到数据库执行
    db.commit()
    # 关闭数据库连接
    db.close()

    print "Created table Successfull."

# 初始化或者调用函数
if __name__ == "__main__":
    chartId = 'componentsByIsp'
    data = get_data(chartId)
    data_insert(data)