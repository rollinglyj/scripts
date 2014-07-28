#!/usr/bin/python
#-*-coding:utf-8-*-

'''
This file include all the common routine,that are needed in
the crawler project.
Author: Justnzhang @(uestczhangchao@qq.com)
Time:2014年7月28日15:03:44
'''

from common_data import *
import sys
import MySQLdb
from urllib import quote, unquote

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

        values.append(dictData[corpName])
        values.append(dictData[registerId])
        values.append(dictData[legalRepre])
        values.append(dictData[residence])
        values.append(dictData[registerCapital])
        values.append(dictData[economicNature])
        values.append(dictData[corpState])
        values.append(dictData[businessMode])
        values.append(dictData[registerAutho])
        values.append(dictData[administraveAutho])
        values.append(dictData[businessScope])
            
        cur_local.execute("insert into shanghai values(NULL,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",values)
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
    dictData[businessMode] = '独立'
    dictData[registerAutho] = '上海'
    dictData[administraveAutho] = '静安'
    dictData[businessScope] = '网络欺诈'
    insertDB(dictData)