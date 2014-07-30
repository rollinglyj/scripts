#!/usr/bin/python  
#-*-coding:utf-8-*- 
import sys

reload(sys)
sys.setdefaultencoding('utf-8') 

firstPageUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch#'
secondPageUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=viewDetail'
refUrl = 'http://www.sgs.gov.cn/lz/etpsInfo.do?method=doSearch'

#flowing are corp infos
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

'''corpName = '名称:'
registerId = '注册号:'
legalRepre = '法定代表人姓名:'
residence = '住所:'
registerCapital = '注册资本:'
economicNature = '公司类型:'
corpState = '企业状态:'
#businessMode = '经营方式'
registerAutho = '登记机关:'
administraveAutho = '受理机关:' 
businessScope =  '经营范围:'
'''

corpName = '名称'
registerId = '注册号'
legalRepre = '法定代表人姓名'
residence = '住所'
registerCapital = '注册资本'
economicNature = '公司类型'
corpState = '企业状态'
#businessMode = '经营方式'
registerAutho = '登记机关'
administraveAutho = '受理机关' 
businessScope =  '经营范围'



MYSQL_CORP_INFO='mysql -hlocalhost -uroot -pMhxzKhl -P3306 -D corp_info -e "'

