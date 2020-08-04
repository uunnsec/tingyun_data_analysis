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
        result[15] = float(result[15]) / 1000
        result[18] = float(result[18]) / 1000
        result[19] = float(result[19]) / 1000
        result[20] = float(result[20]) / 1000
        result[21] = float(result[21]) / 1000
        result[22] = float(result[22]) / 1000
        result[23] = float(result[23]) / 1000
        result[24] = float(result[24]) / 1000
        result[25] = float(result[25]) / 1000
        result[26] = float(result[26]) / 1000
        result[27] = float(result[27]) / 1000
        result[28] = float(result[28]) / 1000
        result[29] = float(result[29]) / 1000
        result[34] = float(result[34]) / 1000
        result[35] = float(result[35]) / 1000
        result[37] = float(result[37]) / 1000
        result[41] = float(result[41]) / 1000
        result[42] = float(result[42]) / 1000
        result[55] = float(result[55]) / 1000
        result[56] = float(result[56]) / 1000
        result[57] = float(result[57]) / 1000
        result[58] = float(result[58]) / 1000
        result[59] = float(result[59]) / 1000

        result1 = [request_val1['taskId']] + result

        insert = "insert into default_original_data(TaskId,Time,PageNumber,Province,City,Isp,AccessMethod,OSVersion," \
                 "BrowserVersion,FlashVersion,DNSServer,MonitoringPointsIP,HostIP,HostCity,HostIsp,WrongDescription," \
                 "TotalDownloadTime,TotalDownloadBytes,DownloadSpeed,FirstScreeTime,DNSTime,EstablishConnectionTime," \
                 "SSLHandshakeTime,RedirectionTime,RequestTime,FirstPackageTime,ContentDownloadTime," \
                 "CloseConnectionTime,ClientTime,NetworkLayerTime,BasicPageDownloadTime,BasicPageDownloadBytes," \
                 "BasicPageDownloadSpeed,FirstScreenObjectsNumber,FirstScreenDownloadBytes,DNSParsingTime," \
                 "DNSParsingTotalTime,EstablishConnectionNumber,EstablishConnectionTotalTime,PageObjectsNumber," \
                 "DOMElementsNumber,IFRAMENumber,ReceivingAdditionalDataTime,PageOpeningTime,ElementErrorQuantity," \
                 "ScriptError,HTTPServer,HTTPVia,NoCompressHeaderElementsNumber,NoExpiresHeaderElementsNumber," \
                 "NoEtagHeaderElementsNumber,AverageCPUUtilization,CurrentTaskCPUUtilization," \
                 "AverageMemoryUtilization,CurrentTaskMemoryUtilization,AverageDownloadSpeed,FirstRenderingTime," \
                 "CustomRenderingTime,DOMProcessingEndTime,OnLoadEventStartTime,OnLoadEventEndTime,HTMLSourceCode)" \
                 "values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s," \
                 "%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
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