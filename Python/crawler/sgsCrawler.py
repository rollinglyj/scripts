#!/usr/bin/python  
#-*-coding:utf-8-*- 
'''
Author: justinzhang
Email:  uestczhangchao@gmail.com/zhangchao3@unionpay.com
2014-7-24 9:44 Thursday
'''
import sys
import os
import time
import datetime
from urllib import unquote
from urllib import quote

def getFirstPage(formData, url, savedFile):
    crawlCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + savedFile + '> log.cmd 2>&1;'
    parseCmd = 'wget --post-data ' +"'"+ formData + "' " + url + ' -O '  + '- -q | ' + 'grep "<a href" | grep viewDetail | '+ "awk '{print $3}' | awk -F'=' '{print $2}' |"+' awk -F\\"'+" '{print $2}' | awk -F'(' '{print $2}' | awk -F\\' '{print $2}'"
#    print crawlCmd
    print parseCmd
#    crawlCmdRe = os.popen(crawlCmd).readlines()
    parseCmdRe = os.popen(parseCmd).readlines()
    for id in parseCmdRe:
        print id.strip()
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
        print i
        newList.append(li.strip().replace(':',''))
        print unquote(newList[i])
        i = i + 1
    print '--invisible divider-----'
    print newList
    corpInfo={}
    print quote('企业名称')
    print quote('企业名称:')
    print newList.index('企业名称')
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    print corpInfo



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
    else:
        print "Usage: Python sgsCrawler.py <formData> <URL> <saveDFile> [<refUrl>]"
