#coding=utf-8
__author__ = 'xiyuanbupt'

import unittest

from statistics.fromLog import getScrapyStatusFromScrapyLog
from statistics.fromSys import getDirSize
from statistics.fromDB import KaoLaStatistics,XmlyStatistics,QtStatistics
from conf_util import ConfUtil

class TestFromLog(unittest.TestCase):

    def testGetJsonStrFromScrapyLog(self):
        getScrapyStatusFromScrapyLog('./test.log')
        getScrapyStatusFromScrapyLog('./example.log')

class TestFromSys(unittest.TestCase):

    def testGetDirSize(self):
        size = getDirSize('.')
        print 'Total Size is %.3f'%(size/1024/1024),'Mbytes'

class TestConf(unittest.TestCase):

    def testConfUtil(self):
        self.assertEqual(ConfUtil.getQTAudioDir(),'/var/crawler/qt/audios/full')
        self.assertEqual(
            ConfUtil.getKLAudioDir(),'/var/crawler/kl/audios/full'
        )

class TestFromDB(unittest.TestCase):

    kl = KaoLaStatistics()
    xmly = XmlyStatistics()
    qt = QtStatistics()

    def testKaolaStatistics(self):
        res = self.kl._getAlbum_AudioCountPerCategory()
        print u'显示格式为对应categoryName 与对应的albumCount 与audioCount'
        for key in res:
            print key,res[key]

    def testGetAlbumCountPerCategory(self):
        res = self.kl.getAlbumCountPerCategory()
        print u'显示的格式为categoryName 对应的 albumCount'
        for key in res:
            print key,res[key]

    def testGetAudioCountPerCategory(self):
        res = self.kl.getAudioCountPerCategory()
        print u'显示的格式为categoryName 对应的audioCount'
        for key in res:
            print key,res[key]

    def testXGetAlbum_AudioCountPerCategory(self):
        res = self.xmly._getAlbum_AudioCountPerCategory()
        for item in res:
            self.assertEqual(len(res[item]),len([1,2]))

    def testXGetAlbumCountPerCategory(self):
        res = self.xmly.getAlbumCountPerCategory()
        print u'显示的内容为当前喜马拉雅数据库中 对应的albumCount '
        for key in res:
            print key , res[key]

    def testXGetAudioCountPerCategory(self):
        res = self.xmly.getAudioCountPerCategory()
        print u'显示的内容为喜马拉雅数据库中对应的audioCount'
        for key in res:
            print key ,res[key]

    def testQGetAlbum_AudioCountPerCategory(self):
        res = self.qt._getAlbum_audioCountPerCategory()
        print u'下面为qt中对应的个数'
        for key in res:
            print key ,res[key]


if __name__ == "__main__":
    unittest.main()
