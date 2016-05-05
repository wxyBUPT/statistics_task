#coding=utf-8
__author__ = 'xiyuanbupt'
import datetime

import tailer

def getScrapyStatusFromScrapyLog(logPath):
    '''
    通过scrapy 的日志获得如下格式的json str，日志内容必须为scrapy 刚执行完成后的日志内容
    2016-05-03 17:07:24 [scrapy] INFO: Dumping Scrapy stats:
    {'downloader/request_bytes': 227847,
     'downloader/request_count': 427,
     'downloader/request_method_count/GET': 427,
     'downloader/response_bytes': 799168,
     'downloader/response_count': 427,
     'downloader/response_status_count/200': 427,
     'finish_reason': 'finished',
     'finish_time': datetime.datetime(2016, 5, 3, 9, 7, 24, 34782),
     'item_scraped_count': 6882,
     'log_count/DEBUG': 7310,
     'log_count/INFO': 16,
     'request_depth_max': 3,
     'response_received_count': 427,
     'scheduler/dequeued': 427,
     'scheduler/dequeued/memory': 427,
     'scheduler/enqueued': 427,
     'scheduler/enqueued/memory': 427,
     'start_time': datetime.datetime(2016, 5, 3, 8, 58, 42, 954245)}
    2016-05-03 17:07:24 [scrapy] INFO: Spider closed (finished)
    :param logPath:
    :return:
    '''
    lines = tailer.tail(open(logPath),50)
    nu = 0
    for i,line in enumerate(lines):
        if line.endswith('Dumping Scrapy stats:'):
            nu = i
    jsonStr = ''.join(lines[nu+1:-1])
    jsonDict = eval(jsonStr)
    return jsonDict
