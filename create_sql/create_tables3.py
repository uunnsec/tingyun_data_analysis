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
          `Time` datetime default NULL,
          `PageNumber` int(10) NOT NULL,
          `Province` varchar(40) NOT NULL,
          `City` varchar(40) NOT NULL,
          `Isp` varchar(40) NOT NULL,
          `AccessMethod` varchar(40) NOT NULL,
          `OSVersion` varchar(40) NOT NULL,
          `BrowserVersion` varchar(40) NOT NULL,
          `FlashVersion` varchar(40) NOT NULL,
          `DNSServer` varchar(40) NOT NULL,
          `MonitoringPointsIP` varchar(40) NOT NULL,
          `HostIP` varchar(40) NOT NULL,
          `HostCity` varchar(40) NOT NULL,
          `HostIsp` varchar(40) NOT NULL,
          `WrongDescription` varchar(40) NOT NULL,
          `TotalDownloadTime` float(40) NOT NULL,
          `TotalDownloadBytes` float(40) NOT NULL,
          `DownloadSpeed` float(40) NOT NULL,
          `FirstScreeTime` float(40) NOT NULL,
          `DNSTime` float(40) NOT NULL,
          `EstablishConnectionTime` float(40) NOT NULL,
          `SSLHandshakeTime` float(40) NOT NULL,
          `RedirectionTime` float(40) NOT NULL,
          `RequestTime` float(40) NOT NULL,
          `FirstPackageTime` float(40) NOT NULL,
          `ContentDownloadTime` float(40) NOT NULL,
          `CloseConnectionTime` float(40) NOT NULL,
          `ClientTime` float(40) NOT NULL,
          `NetworkLayerTime` float(40) NOT NULL,
          `BasicPageDownloadTime` float(40) NOT NULL,
          `BasicPageDownloadBytes` float(40) NOT NULL,
          `BasicPageDownloadSpeed` float(40) NOT NULL,
          `FirstScreenObjectsNumber` float(40) NOT NULL,
          `FirstScreenDownloadBytes` float(40) NOT NULL,
          `DNSParsingTime` float(40) NOT NULL,
          `DNSParsingTotalTime` float(40) NOT NULL,
          `EstablishConnectionNumber` float(40) NOT NULL,
          `EstablishConnectionTotalTime` float(40) NOT NULL,
          `PageObjectsNumber` float(40) NOT NULL,
          `DOMElementsNumber` float(40) NOT NULL,
          `IFRAMENumber` float(40) NOT NULL,
          `ReceivingAdditionalDataTime` float(40) NOT NULL,
          `PageOpeningTime` float(40) NOT NULL,
          `ElementErrorQuantity` float(40) NOT NULL,
          `ScriptError` varchar(100) NOT NULL,
          `HTTPServer` varchar(40) NOT NULL,
          `HTTPVia` varchar(40) NOT NULL,
          `NoCompressHeaderElementsNumber` float(40) NOT NULL,
          `NoExpiresHeaderElementsNumber` float(40) NOT NULL,
          `NoEtagHeaderElementsNumber` float(40) NOT NULL,
          `AverageCPUUtilization` float(40) NOT NULL,
          `CurrentTaskCPUUtilization` float(40) NOT NULL,
          `AverageMemoryUtilization` float(40) NOT NULL,
          `CurrentTaskMemoryUtilization` float(40) NOT NULL,
          `AverageDownloadSpeed` float(40) NOT NULL,
          `FirstRenderingTime` float(40) NOT NULL,
          `CustomRenderingTime` float(40) NOT NULL,
          `DOMProcessingEndTime` float(40) NOT NULL,
          `OnLoadEventStartTime` float(40) NOT NULL,
          `OnLoadEventEndTime` float(40) NOT NULL,
          `HTMLSourceCode` varchar(40) NOT NULL,
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