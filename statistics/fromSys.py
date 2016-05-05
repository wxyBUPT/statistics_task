#coding=utf-8
__author__ = 'xiyuanbupt'

import os
from os.path import join,getsize

def getDirSize(dir):
    size = 0L
    for root, dirs,files in os.walk(dir):
        size += sum([getsize(join(root,name)) for name in files])
    return size
