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
        tmp = li.strip().replace(':','')
        tmp = tmp.replace('&nbsp;','')
        newList.append(tmp)

    corpInfo={}
    corpInfo['企业名称'] = newList[newList.index('企业名称') + 1]
    corpInfo['注册号'] = newList[newList.index('注册号') + 1]
    corpInfo['法定代表人'] = newList[newList.index('法定代表人') + 1]
    corpInfo['住所'] = newList[newList.index('住所') + 1]
    corpInfo['注册资金'] = newList[newList.index('注册资金') + 1]
    corpInfo['经济性质'] = newList[newList.index('经济性质') + 1]
    corpInfo['企业状态'] = newList[newList.index('企业状态') + 1]
    corpInfo['经营方式'] = newList[newList.index('经营方式') + 1]
    corpInfo['登记机关'] = newList[newList.index('登记机关') + 1]
    corpInfo['受理机关'] = newList[newList.index('受理机关') + 1]
    corpInfo['经营范围'] = newList[newList.index('经营范围') + 1]

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
    else:
        print "Usage: Python sgsCrawler.py <formData> <URL> <saveDFile> [<refUrl>]"
