#!/home/udwrt/dstream/utils/python2.6/bin/python

#  --*-- URL --*--
url = {
    'HOST'    :    'db-dstream-online.dmop.baidu.com:8008',
    'PEMAP'      :    '/api_app_pe.php?',
    'PIPE2PE'  : '/pipe2pe.php?',
    'TABLES'   :   [ 
        '/log_metrics.php?do=view&view=QPS&show=txt', # QPS
        '/log_metrics.php?do=view&view=QWatcher&show=txt', #Queue size
    ]
}
#  --*-------------*--

#  --*- RECEIVER --*--
#MailList   = 'udwrt_mon@baidu.com, manzhengrui@baidu.com, sunhuali01@baidu.com, lintao02@baidu.com, liwen03@baidu.com'
#MobileList = ('18616523553','13774299598', '13918040665', '15911186897', '13733123468', '13965044377', '13810620464', '18301956105', 
#             '15201210051', # sunhuali
#             '18801294127', #lintao 
#             '15829385048'  #liwen
#             )
#  --*-------------*--
#MailList   = 'wangzhiqing@baidu.com'
#MobileList = ('13918040665', '18628354938')

MailList    = ''
MobileList = ();

#  --*-- PARAMETER --*--
LookBackSeconds = 65
LookBackRows = 1000
#appid = 11 
appname = 'UDW_RT_141'
RetryTimes = 5
SleepSeconds = 60 
#  --*---------------*--

#  --*--  ALARMS  --*--
alarms = {
    'default_alarms' : {
        'SEND'     :    [ 'value',    '<',    '0',   3], # alarm if value < 5000 & occured 3 times in succession
        'RECV'     :    [ 'value',    '<',    '0',   5],
        'RQUEUE'   :    [ 'queue_size',  '>=',    '0',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',     '1',  7],
    },

    'runse_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '<',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },

    'runps_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },

    'runtb_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
    
    'runtb_importer2' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
    
    'ers_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
 
    'logcenter_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
 
    'logs-apache_importer_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },    
    
    'rtpe' : {
        'SEND'     :    [ 'value',    '<',    '1',  10], 
        'RECV'     :    [ 'value',    '<',    '1',  10], 
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },

    'dmf_ers' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '1',    10],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },

    'dmf_ers2' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '1',    10],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },

    'dmf_mob' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '1',    10],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },

    'lbstag_exporter' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '1',    10],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },

    'click_exporter' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '0',     1],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },

    'applist_exporter' : {
	'SEND'	   :    [ 'value',    '!=',    '0',    1],
	'RECV'	   :    [ 'value',    '<',    '0',     1],
	'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
	'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },
    
    'importer4PS' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
    
    'runlbs_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
    },
    
    'rt_exporter_rp_suim' : {
        'SEND'     :    [ 'value',    '!=',    '0',    1],
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
        'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },
    
    'rt_exporter_rp_rtdm' : {
        'SEND'     :    [ 'value',    '!=',    '0',    1],
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
        'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    },
    
    'rt_exporter_rp_mapselbs' : {
        'SEND'     :    [ 'value',    '!=',    '0',    1],
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size', '>', '10000',  5],
        'SQUEUE'   :    [ 'queue_size', '>', '10000',  5],
    }, 
}

nullpipelet = (
'12107512808192',
'12107512807680',
'12107512808448',
'12137577578752',
'12137577579520',
'12137577579264',
)

sparsepipelet          = (
'12137577578496'
'12137577579008',
'12107512807936',
'12107512807424',
)
pe_name_and_pipelet_id_bk = {
'0':['applist_exporter',1],  #pe_name : pipelet_id
'1':['click_exporter',1],
'2':['dmf_ers',1],
'3':['dmf_ers2',1],
'4':['dmf_mob',1],
'5':['ers_importer',1],
'6':['importer4PS',1],
'7':['lbstag_exporter',1],
'8':['log_center_importer',1],
'9':['logs-apache_importer',1],
'10':['rt_exporter_rp_mapselbs',1],
'11':['rt_exporter_rp_rtdm',1],
'12':['rt_exporter_rp_suim',1],
'13':['rtpe',1],
'14':['runlbs_importer',1],
'15':['runps_importer',1],
'16':['runse_importer',1],
'17':['runtb_importer',1],
}

pe_name_and_pipelet_id = {
'0':['applist_exporter',4],  #pe_name : pipelet_id
'1':['click_exporter',4],
'2':['dmf_ers',23],
'3':['dmf_ers2',23],
'4':['dmf_mob',11],
'5':['ers_importer',5],
'6':['importer4PS',12],
'7':['lbstag_exporter',4],
'8':['log_center_importer',7],
'9':['logs-apache_importer',7],
'10':['rt_exporter_rp_mapselbs',17],
'11':['rt_exporter_rp_rtdm',10],
'12':['rt_exporter_rp_suim',36],
'13':['rtpe',79],
'14':['runlbs_importer',21],
'15':['runps_importer',12],
'16':['runse_importer',32],
'17':['runtb_importer',5],
}


#for i in range (0,17):
#    print str(pe_name_and_pipelet_id[str(i)]) + 'should be............'


#  --*--------------*--

import httplib
import time
import os

HOSTNAME = os.popen('echo $HOSTNAME').read().split('.')[0];

pemap = {}
peid_to_name = {}
peid_list = []

def main():
    alarmsleep = SleepSeconds
    retrycount = 0
    candi      = {}
    ret        = {}
    dict1      = {}
    
    conn       = httplib.HTTPConnection(url['HOST'])
    conn.request('GET','/ajax/app_name2id.php?name='+appname)
    global appid
    dict1      = (conn.getresponse().read())
    dict1      = eval(dict1)
    appid = dict1["id"]
    conn.request('GET', url['PEMAP']+'appid='+str(appid))
#    print '%s' % (url['PEMAP']+'appid='+str(appid))
#    print '%s' % (conn.getresponse().read())
    global pemap
    pemap = dict(map(lambda x:x.split('|'), conn.getresponse().read().strip().split('\n')))

#    for i in range(0,18):
#        pe_name_pipelet_id_list = pe_name_and_pipelet_id[str(i)]
#        print str(i)+':'+ pe_name_pipelet_id_list[0]+':' + str(pe_name_pipelet_id_list[1])
#       print url['PIPE2PE']
#        for j in range(0,pe_name_pipelet_id_list[1]):
#           conn.request('GET',url['PIPE2PE'] + 'pe_name=' + pe_name_pipelet_id_list[0] + '&pipelet_id=' + str(j))
#           pe_id                = conn.getresponse().read() 
#           global peid_to_name 
#           print pe_name_pipelet_id_list[0] + '_' + str(j) + ':' + 'peid=' + pe_id
#           peid_to_name[pe_id]  = pe_name_pipelet_id_list[0]
#           print 'pe_id=' + pe_id + 'peid_name:' + peid_to_name[pe_id]
#           peid_list.append(pe_id)
#           for pe_id_item in peid_list:
#               print 'pe_id_item:' + pe_id_item + ' '
#               print peid_to_name[pe_id_item]

#   Print pemap

    while True:
        try:
            ret = getalarms()
            retrycount = 0
            for key in ret:
                if(candi.has_key(key)):
                    ret[key][0] += candi[key][0]
            candi = ret
        except:
            retrycount += 1
        if retrycount > RetryTimes:
            print '%s==> CANNOT GET DATA. RETRYCOUNT:%d' % (HOSTNAME, retrycount)
            doalarm('%s==> CANNOT GET DATA. RETRYCOUNT:%d' % (HOSTNAME, retrycount))
            alarmsleep *=1.5
        else:
            out = ''
            for key in ret:
                if(ret[key][0] >= ret[key][1]):
                    out += '%s==>%s:%s:%s:%d\r\n' % (HOSTNAME, ret[key][2], key, ret[key][3], ret[key][0])                    
                    # time:PEID:type(upstream PEID):value:retrycount
            if out == '':
                print time.ctime(time.time()) + ': OK'
                alarmsleep = SleepSeconds
            else:
                print out[:-1]
                doalarm(out[:-1])
                alarmsleep *= 1.5
        time.sleep(alarmsleep)

def doalarm(msg):
    mailalarm = 'echo "%s"|mail -s "QPS or Qsize Alarm" %s' % (msg, MailList)
    os.system(mailalarm)
    for mobile in MobileList:
        mobilealarm = 'gsmsend -s tc-sys-monitor00.tc:15001 -s tc-sys-monitor01.tc:15001 *2*%s@"%s"' % (mobile, msg)
        os.system(mobilealarm)

def getalarms():
    conn = httplib.HTTPConnection(url['HOST'])
    out  = {}
    for table in url['TABLES']:
#        conn.request('GET', table+'&limit=0,'+str(LookBackRows+1)+'&where=appid='+str(appid)+'%20and%20time%3E'+str(int(time.time())-LookBackSeconds))
#        print '%s' % (table+'&limit=0,'+str(LookBackRows+1)+'&where=appid='+str(appid)+'%20and%20time%3E'+str(int(time.time())-LookBackSeconds))
        conn.request('GET','/log_metrics.php?do=view&view=QPS&show=txt&limit=0,1001&where=appid=11%20and%20time%3E1364983191')

        data = conn.getresponse().read().strip().split('\n')
        title = data.pop(0).split('|')

        data = map(lambda x:x.split('|'), data)
        data.sort(key=lambda x:x[title.index('time')])
#        print data
        
        for line in data:
            items = dict(zip(title, line))
#            if items['PEID'] in nullpipelet:
#                continue
#           if items['PEID'] in sparsepipelet and time.gmtime()[3] < 24 and time.gmtime()[3] > 17:
#               continue

            print items
            print type(items)
            print 'PEID=:'
            print items['PEID']
            print 'type=:'
            print items['type']
            print 'value=:'
            print items['value']
            print 'name=:'
#            print peid_to_name[items['PEID']]
            
            uplen = 1
#            if items.has_key('owners'):        
#                uplen = max(uplen, len(items['owners'].split(',')) - 1)
            petype    = pemap[items['PEID']]
            print petype
            print '%s_%s_%s:%s' % (petype,items['type'],items['PEID'],items['value'])
#            try:
#                alarm = alarms[petype][items['type']]
#            except:            
#                if alarms['default_alarms'].has_key(items['type']):
#                    alarm = alarms['default_alarms'][items['type']]
#                else:
#                    continue

#            if eval(items[alarm[0]]+alarm[1]+alarm[2]+'*'+str(uplen)):
#                out['%s:%s(%s)' % (items['PEID'], items['type'], items.get('owners', ''))] = \
#                        [1, alarm[3], time.ctime(int(items['time'])), items[alarm[0]]]
    return "" 

if __name__=='__main__':
    main()

