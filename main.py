#coding=utf-8
__author__ = 'xiyuanbupt'

from collections import defaultdict,Counter

from pymongo import MongoClient
import logging
import logging.config

from conf_util import ConfUtil
from statistics.fromDB import KaoLaStatistics,XmlyStatistics,QtStatistics
from statistics.fromSys import getDirSize

client = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
db = client[ConfUtil.getStatisticsDBName()]

class Main:
    coll = db[ConfUtil.getStatisticCronPerHourCollection()]

    def __init__(self):
        self.klSt = KaoLaStatistics()
        self.qtSt = QtStatistics()
        self.xmlySt = XmlyStatistics()

    def runOnce(self):
        '''
        执行一次统计任务
        :return:
        '''
        kl = self.runForKL()
        qt = self.runForQt()
        xmly = self.runForXMLY()
        forInsert = dict(
            kl = kl,
            qt = qt,
            xmly = xmly
        )
        self.coll.insert(forInsert)

    def runForKL(self):
        '''
        执行考拉的统计任务
        :return:
        '''
        #根据系统统计文件大小
        audio_dir = ConfUtil.getKLAudioDir()
        image_dir = ConfUtil.getKLImageDir()
        res = defaultdict()
        res['totalAudioSize(bytes)'] = getDirSize(audio_dir)
        res['totalImageSize(bytes)'] = getDirSize(image_dir)

        #根据数据库统计专辑与媒体文件的数量
        res['totalAlbumCount'] = self.klSt.getAlbumCount()
        res['totalAudioCount'] = self.klSt.getAudioCount()

        res['audioCountPerCategory'] = self.klSt.getAudioCountPerCategory()
        res['albumCountPerCategory'] = self.klSt.getAlbumCountPerCategory()
        return res

    def runForQt(self):
        '''
        执行qt 统计任务
        :return:
        '''
        audio_dir = ConfUtil.getQTAudioDir()
        image_dir = ConfUtil.getQTImageDir()
        res = defaultdict()
        res['totalAudioSize(bytes)'] = getDirSize(audio_dir)
        res['totalImageSize(bytes)'] = getDirSize(image_dir)

        res['totalAlbumCount'] = self.qtSt.getAlbumCount()
        res['totalAudioCount'] = self.qtSt.getAudioCount()

        res['audioCountPerCategory'] = self.qtSt.getAudioCountPerCategory()
        res['albumCountPerCategory'] = self.qtSt.getAlbumCountPerCategory()
        return res

    def runForXMLY(self):
        '''
        执行喜马拉雅统计任务
        :return:
        '''
        audio_dir = ConfUtil.getXMLYAudioDir()
        image_dir = ConfUtil.getXmlyImageDir()
        res = defaultdict()
        res['totalAudioSize(bytes)'] = getDirSize(audio_dir)
        res['totalImageSize(bytes)'] = getDirSize(image_dir)

        res['totalAlbumCount'] = self.xmlySt.getAlbumCount()
        res['totalAudioCount'] = self.xmlySt.getAudioCount()

        res['audioCountPerCategory'] = self.xmlySt.getAudioCountPerCategory()
        res['albumCountPerCategory'] = self.xmlySt.getAlbumCountPerCategory()
        return res

if __name__ == "__main__":
    main = Main()
    main.runOnce()
