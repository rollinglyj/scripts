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
from common_data import firstPageUrl, secondPageUrl, refUrl,corpName,registerId,\
legalRepre,residence,registerCapital,economicNature,corpState,businessMode,\
registerAutho,administraveAutho,businessScope


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

def getFirstPage(formData, url, savedFile):
    etpsIdList=[]
    crawlCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + savedFile + '> log.cmd 2>&1;'
    parseCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + '- -q | ' + 'grep "<a href" | grep viewDetail | '+ "awk '{print $3}' | awk -F'=' '{print $2}' |"+' awk -F\\"'+" '{print $2}' | awk -F'(' '{print $2}' | awk -F\\' '{print $2}'"
#    print crawlCmd
    print parseCmd
#    crawlCmdRe = os.popen(crawlCmd).readlines()
    parseCmdRe = os.popen(parseCmd).readlines()
    for id in parseCmdRe:
#        print id.strip()
        etpsIdList.append(id.strip())
    return etpsIdList
#    print parseCmdRe


def getSecondPage(formData, url, savedFile, refUrl):
#    crawlCmd = 'wget --post-data ' + "'" + formData + "' " + "--referer " + refUrl + " " + url + ' -O ' + savedFile + ' > log2.cmd 2>&1;'
    crawlCmd2 = 'wget --post-data ' + "'" + formData + "' " + "--referer " + refUrl + " " + url + ' -O ' + '- -q |' + "grep '<td' | sed 's/<[^<]*>//g'" 
    print crawlCmd2
    crawlCmdRe = os.popen(crawlCmd2).readlines()
    strs = unquote(''.join(crawlCmdRe))
    i = 0
    print crawlCmdRe
    newList = []
    for li in crawlCmdRe:
        tmp = li.strip().replace(':','')
        tmp = tmp.replace('&nbsp;','')
        newList.append(tmp)

    corpInfo={}
    corpInfo[corpName] = newList[newList.index(corpName) + 1]
    corpInfo[registerId] = newList[newList.index(registerId) + 1]
    corpInfo[legalRepre] = newList[newList.index(legalRepre) + 1]
    corpInfo[residence] = newList[newList.index(residence) + 1]
    corpInfo[registerCapital] = newList[newList.index(registerCapital) + 1]
    corpInfo[economicNature] = newList[newList.index(economicNature) + 1]
    corpInfo[corpState] = newList[newList.index(corpState) + 1]
    corpInfo[businessMode] = newList[newList.index(businessMode) + 1]
    corpInfo[registerAutho] = newList[newList.index(registerAutho) + 1]
    corpInfo[administraveAutho] = newList[newList.index(administraveAutho) + 1]
    corpInfo[businessScope] = newList[newList.index(businessScope) + 1]

    for (k, v) in corpInfo.items():
        print '['+unquote(k) +':' + unquote(v) + ']'



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
        getInfoByEtpsId(sys.argv[1])
    else:
        print "Usage: Python sgsCrawler.py <formData> <URL> <saveDFile> [<refUrl>]"
