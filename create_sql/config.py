#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import datetime
today = datetime.date.today()
oneday = datetime.timedelta(days=1)
yesterday = today - oneday
now_time = (datetime.datetime.now()+datetime.timedelta(hours=-1)).strftime("%Y-%m-%d %H")
times = yesterday

chartId = {
    'componentsByTask': 'general',
    'componentsByProv': 'province',
    'componentsByProvIsp': 'prov_isp',
    'componentsByLocation': 'city',
    'componentsByLocationIsp': 'city_isp',
    'componentsByTime': 'time',
    'componentsWeightByTask': 'weight'
}


request_val = {
    'taskId': '21***57',
    'absoluteTimeFrom': '%s 00:00' % yesterday,
    'absoluteTimeTo': '%s 23:59' % yesterday,
}

request_val1 = {
    'taskId': '21***57',
    'absoluteTimeFrom': '%s:00' % now_time,
    'absoluteTimeTo': '%s:59' % now_time,
}

mysql_val = {
    'host': '192.168.1.3',
    'port': 3306,
    'user': 'tingyun',
    'password': 'Tingyun@2019data',
    'db': 'tingyun',
    'charset': 'utf8'
}

tables1 = [
    'city',
    'city_isp',
    'isp',
    'general',
    'weight'
]

tables2 = [
    'province',
    'prov_isp'
]

tables3 = ['default_original_data']

tables4 = ['time']
