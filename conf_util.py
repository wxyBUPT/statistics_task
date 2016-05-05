#coding=utf-8
__author__ = 'xiyuanbupt'
import ConfigParser
import os.path

cf = ConfigParser.ConfigParser()
cf.read('global.ini')

class ConfUtil:

    @classmethod
    def getQTAudioDir(cls):
        return cf.get('qingting','audio_dir')

    @classmethod
    def getKLAudioDir(cls):
        return cf.get('kaola','audio_dir')

    @classmethod
    def getXMLYAudioDir(cls):
        return cf.get('ximalaya','audio_dir')

    @classmethod
    def getMongoIP(cls):
        return cf.get('mongo','ip')

    @classmethod
    def getMongoPort(cls):
        return cf.getint('mongo','port')

    @classmethod
    def getStatisticsDBName(cls):
        return cf.get('mongo','statistics_db')

    @classmethod
    def getSpiderDBName(cls):
        return cf.get('mongo','spider_db')

    @classmethod
    def getCrontabCollectionName(cls):
        return cf.get('mongo','crontab')

    @classmethod
    def getXMLYAlbumCollectionName(cls):
        return cf.get('spider_collections','xmly_album')

    @classmethod
    def getXMLYCategoryCollectionName(cls):
        return cf.get('spider_collections','xmly_category')

    @classmethod
    def getKLAlbumCollectionName(cls):
        return cf.get('spider_collections','kl_album')

    @classmethod
    def getKLCategoryCollectionName(cls):
        return cf.get('spider_collections','kl_category')

    @classmethod
    def getQTAlbumCollectionName(cls):
        return cf.get('spider_collections','qt_item')

    @classmethod
    def getXMLYAudioCollectionName(cls):
        '''
        获得存储xmly 所有audio 信息的collection
        :return:
        '''
        return cf.get('spider_collections','xmly_audio')

    @classmethod
    def getKLAudioCollectionName(cls):
        return cf.get('spider_collections','kl_audio')

    @classmethod
    def getQTAudioCollectionName(cls):
        return cf.get('spider_collections','qt_audio')

    @classmethod
    def getStatisticCronPerHourCollection(cls):
        return cf.get('statistics_collections','media_summary')

    @classmethod
    def getKLImageDir(cls):
        return cf.get('kaola','image_dir')

    @classmethod
    def getQTImageDir(cls):
        return cf.get('qingting','image_dir')

    @classmethod
    def getXmlyImageDir(cls):
        return cf.get('ximalaya','image_dir')

    @classmethod
    def getCrawlHistoryCollectionName(cls):
        return cf.get('statistics_collections','crawl_history')

    @classmethod
    def getTestLogDir(cls):
        return cf.get('test','logDir')

    @classmethod
    def getTestCrawler(cls):
        return cf.get('test','crawler')