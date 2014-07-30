#!/usr/bin/python
#-*-coding:utf-8-*-

'''
This file include all the common routine,that are needed in
the crawler project.
Author: Justnzhang @(uestczhangchao@qq.com)
Time:2014年7月28日15:03:44
'''
import os
from common_data import *
import sys
import MySQLdb
from urllib import quote, unquote
from bs4 import BeautifulSoup

'''corpName = '企业名称'
registerId = '注册号'
legalRepre = '法定代表人'
residence = '住所'
registerCapital = '注册资金'
economicNature = '经济性质'
corpState = '企业状态'
businessMode = '经营方式'
registerAutho = '登记机关'
administraveAutho = '受理机关' 
businessScope =  '经营范围'
'''

def newParser(formData, url, savedFile, refUrl):
    crawlCmd2 = 'wget --post-data ' + "'" + formData + "' " + "--referer " + refUrl + " " + url + ' -O ' + '- -q '
    parseCmdRe = os.popen(crawlCmd2).readlines()
    print crawlCmd2
    strs = ''.join(parseCmdRe)
    soup = BeautifulSoup(strs)
    newList = []
    for td in soup.find_all('td'):
        tmp = td.string
        if(tmp is None):
            continue
        else:
            tmp = tmp.strip().replace(':','')
            newList.append(tmp)
    print newList
    corpInfo={}
    corpInfo[corpName] = newList[newList.index(corpName) + 1]
    corpInfo[registerId] = newList[newList.index(registerId) + 1]
    corpInfo[legalRepre] = newList[newList.index(legalRepre) + 1]
    corpInfo[residence] = newList[newList.index(residence) + 1]
    corpInfo[registerCapital] = newList[newList.index(registerCapital) + 1]
    corpInfo[economicNature] = newList[newList.index(economicNature) + 1]
    corpInfo[corpState] = newList[newList.index(corpState) + 1]
#    corpInfo[businessMode] = newList[newList.index(businessMode) + 1]
    corpInfo[registerAutho] = newList[newList.index(registerAutho) + 1]
    corpInfo[administraveAutho] = newList[newList.index(administraveAutho) + 1]
    corpInfo[businessScope] = newList[newList.index(businessScope) + 1]
    displayDict(corpInfo)


def displayDict(maps):
    for (k, v) in maps.items():
        print '['+unquote(k) +':' + unquote(v) + ']'


def displayInfo(recordNum):
    try:
        conn_local = MySQLdb.connect(host='localhost',user='root',passwd='MhxzKhl',db='corp_info',port=3306)
        cur_local = conn_local.cursor()
        cur_local.execute('select * from shanghai limit ' + recordNum)
        results     = cur_local.fetchall();
        for row in results:
            for i in row:
                print str(i)+ " ",
            print    
        conn_local.commit()
        cur_local.close()
        conn_local.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

def insertDB(dictData):
    try:
        conn_local = MySQLdb.connect(host='localhost',user='root',passwd='MhxzKhl',db='corp_info',port=3306)
        cur_local = conn_local.cursor()
        cur_local.execute('select * from shanghai limit 100')
        results     = cur_local.fetchall();
        for row in results:
            for i in row:
                print str(i)+ " ",
            print
        values = []
        print values
        values.append(dictData[corpName])
        values.append(dictData[registerId])
        values.append(dictData[legalRepre])
        values.append(dictData[residence])
        values.append(dictData[registerCapital])
        values.append(dictData[economicNature])
        values.append(dictData[corpState])
#        values.append(dictData[businessMode])
        values.append(dictData[registerAutho])
        values.append(dictData[administraveAutho])
        values.append(dictData[businessScope])
            
        cur_local.execute("insert into shanghai values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
        #print "invinsible seperator line-----------------------------------"
        conn_local.commit()
        cur_local.close()
        conn_local.close()
    except MySQLdb.Error,e:
        print "Mysql Error %d: %s" % (e.args[0], e.args[1])

if __name__ == '__main__':
    dictData = {}
    a='百度'
    dictData[corpName] =  a
    dictData[registerId] = '33333'
    dictData[legalRepre] = 'shixx'
    dictData[residence] = 'xxx'
    dictData[registerCapital] = '3434556.999'
    dictData[economicNature] = '独立'
    dictData[corpState] = '确立'
    #dictData[businessMode] = '独立'
    dictData[registerAutho] = '上海'
    dictData[administraveAutho] = '静安'
    dictData[businessScope] = '网络欺诈'
#    insertDB(dictData)
    if len(sys.argv)==5:
        formData = sys.argv[1]
        url = sys.argv[2]
        savedFile = sys.argv[3]
        refUrl = sys.argv[4]
        newParser(formData, url, savedFile, refUrl)
    
