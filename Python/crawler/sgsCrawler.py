#!/usr/bin/python  
#-*-coding:utf-8-*- 

'''

Author: justinzhang
Email:  uestczhangchao@gmail.com/zhangchao3@unionpay.com
2014-7-24 9:44 Thursday

'''
import MySQLdb
import sys
import os
import time
import datetime
from urllib import unquote
from urllib import quote
from common_data import *
from common_lib import *

reload(sys)
sys.setdefaultencoding('utf-8')


def etlToDB(corpName):
    etpsIdList = getByCorpName(corpName)
    if(len(etpsIdList) != 0):
        for id in etpsIdList:
            dictInfo = getInfoByEtpsId(id)
            insertDB(dictInfo)
            break

'''
Get detail corp info through etpsId
@return: map
'''
def getInfoByEtpsId(etpsId):
    formData = 'etpsId=' + etpsId
    url = secondPageUrl
    savedFile="dumm2.txt"
    retMap = getSecondPage(formData, url, savedFile, refUrl)
    return retMap
    

'''
This function is used to get corp info by corpName.
get etpsid list
@Return: List
'''
def getByCorpName(corpName):
    formData = 'searchType=1&keyWords='+quote(corpName)
    url = firstPageUrl
    savedFile = "dummy.txt"
    etpsIdList = getFirstPage(formData, url, savedFile)
    print etpsIdList
    return etpsIdList





if __name__ == '__main__':
    if len(sys.argv)==5:
        formData = sys.argv[1]
        url = sys.argv[2]
        savedFile = sys.argv[3]
        refUrl = sys.argv[4]
        getSecondPage(formData, url, savedFile, refUrl)
    elif len(sys.argv)==4:
        formData = sys.argv[1]
        url = sys.argv[2]
        savedFile = sys.argv[3]
        getFirstPage(formData, url, savedFile)
    elif len(sys.argv)==2:
#        getByCorpName(sys.argv[1])
        corpInfo = getInfoByEtpsId(sys.argv[1])
        displayDict(corpInfo)

    else:
        print "Usage: Python sgsCrawler.py <formData> <URL> <saveDFile> [<refUrl>]"
