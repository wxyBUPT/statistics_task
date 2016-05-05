#coding=utf-8
__author__ = 'xiyuanbupt'
import argparse
from pymongo import MongoClient

from statistics.fromLog import getScrapyStatusFromScrapyLog
from conf_util import ConfUtil

tClient = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
tDb = tClient[ConfUtil.getStatisticsDBName()]

'''
本脚本为在爬虫爬取相关数据之后通过日志统计相关信息
信息形式如下
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

并将结果推送到mongo 中存储
'''
def getSaveScrapyStatusFromLog(logfile,crawler):
    res = getScrapyStatusFromScrapyLog(logfile)
    res['crawler'] = crawler
    coll = tDb[ConfUtil.getCrawlHistoryCollectionName()]
    coll.insert(res)



if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=u'提取scrapy 日志中的信息并存储到mongo中')
    parser.add_argument(
    '-f',dest='logfile',action='store',help = u'日志路径，该日志必须为scrapy执行完毕而产生的日志',
    metavar = 'logfile',required = True
    )
    parser.add_argument(
    '-t',metavar = 'crawler',action = 'store',dest = 'crawler',
    help = u'产生日志文件的爬虫',required = True
    )
    args = parser.parse_args()
    getSaveScrapyStatusFromLog(args.logfile,args.crawler)

