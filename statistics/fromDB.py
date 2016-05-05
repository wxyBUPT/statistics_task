#coding=utf-8
__author__ = 'xiyuanbupt'

from collections import defaultdict

from pymongo import MongoClient

from conf_util import ConfUtil

tmpClient = MongoClient(ConfUtil.getMongoIP(),ConfUtil.getMongoPort())
sDb = tmpClient[ConfUtil.getSpiderDBName()]

class KaoLaStatistics:
    klAudio = sDb[ConfUtil.getKLAudioCollectionName()]
    klAlbum = sDb[ConfUtil.getKLAlbumCollectionName()]

    def __init__(self):
        self.perCategoryRes = None

    #获得每个类别下的 album 总数以及 audio 总数
    def _getAlbum_AudioCountPerCategory(self):
        res = defaultdict()
        cursor = self.klAlbum.aggregate(
            [
                {
                    "$group":{
                        "_id":"$categoryName",
                        "totalAudio":{"$sum":"$audioCounts"},
                        "totalAlbum":{"$sum":1},
                    }
                }
            ]
        )
        for item in cursor:
            res.update({item['_id']:[item['totalAlbum'],item['totalAudio']]})
        self.perCategoryRes = res
        return res

    def getAlbumCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_AudioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][0]})
        return res

    def getAudioCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_AudioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][1]})
        return res

class XmlyStatistics:

    xmlyAlbum = sDb[ConfUtil.getXMLYAlbumCollectionName()]

    def __init__(self):
        self.perCategoryRes = None

    def _getAlbum_AudioCountPerCategory(self):
        res = defaultdict()
        cursor = self.xmlyAlbum.aggregate(
            [
                {
                    "$project":{
                        "categoryName":1,
                        "audioCount":{
                            "$size":"$audios"
                        }
                    }
                },
                {
                    "$group":{
                        "_id":"$categoryName",
                        "totalAudio":{"$sum":"$audioCount"},
                        "totalAlbum":{"$sum":1}
                    }
                }
            ]
        )
        for item in cursor:
            res.update({item['_id'].lstrip(u'【').rstrip(u'】'):[item['totalAlbum'],item['totalAudio']]})
        self.perCategoryRes = res
        return res

    def getAlbumCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_AudioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][0]})
        return res

    def getAudioCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_AudioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][1]})
        return res

class QtStatistics:

    qtAlbum = sDb[ConfUtil.getQTAlbumCollectionName()]

    def __init__(self):
        self.perCategoryRes = None

    def _getAlbum_audioCountPerCategory(self):
        res = defaultdict()
        cursor = self.qtAlbum.aggregate(
            [
                {
                    "$project":{
                        "categoryName":"$category",
                        "audioCount":{
                            "$size":"$audios"
                        }
                    }
                },
                {
                    "$group":{
                        "_id":"$categoryName",
                        "totalAudio":{"$sum":"$audioCount"},
                        "totalAlbum":{"$sum":1}
                    }
                }
            ]
        )
        for item in cursor:
            res[item['_id']] = [item['totalAlbum'],item['totalAudio']]
        self.perCategoryRes = res
        return res

    def getAlbumCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_audioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][0]})
        return res

    def getAudioCountPerCategory(self):
        if self.perCategoryRes:
            tmp = self.perCategoryRes
        else:
            tmp = self._getAlbum_audioCountPerCategory()
        res = defaultdict()
        for item in tmp:
            res.update({item:tmp[item][1]})