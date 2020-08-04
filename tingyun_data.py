#!/usr/bin/env python
#-*- coding: UTF-8 -*-
import json
from pprint import pprint
import requests
from config import request_val, request_val1

def get_data(chartId):
    # 使用听云接口获取数据，格式化为json格式
    url = 'http://api.networkbench.com/chartapi/getChartData.do' \
          '?type=json&authkey=nTaCe3ykMD&chartId=%s&taskId=%s&timeRangeMode=Absolute' \
          '&absoluteTimeFrom=%s&absoluteTimeTo=%s' % (chartId, request_val['taskId'], request_val['absoluteTimeFrom'], request_val['absoluteTimeTo'])
    req = requests.get(url, timeout=20)
    data = req.content
    data = json.loads(data, encoding='utf-8')
    # pprint (data['list']['NBChart'][0]['chart-data']['serieses']['series'][0]['rows']['row'][0]['cols']['col'][0]['value'])
    return data

def get_data1():
    url = 'http://dfeed.networkbench.com/rpc-export/exportTxt.po' \
          '?authkey=nTaCe3ykMD&taskId=%s&startDate=%s&endDate=%s' \
          % (request_val1['taskId'], request_val1['absoluteTimeFrom'], request_val1['absoluteTimeTo'])
    req = requests.get(url, timeout=20)
    data = req.content
    return data
