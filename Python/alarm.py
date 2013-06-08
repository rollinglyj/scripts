#!/home/udwrt/dstream/utils/python2.6/bin/python

#  --*-- URL --*--
url = {
    'HOST'    :    'db-dstream-online.dmop.baidu.com:8008',
    'PEMAP'      :    '/api_app_pe.php?',
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
#            '18801294127', #lintao 
#            '15829385048'  #liwen
#            )

MailList  = 'zhangchao08@baidu.com'
MobileList = ('18628354938',)



#  --*-------------*--


#  --*-- PARAMETER --*--
LookBackSeconds = 15
LookBackRows = 100
appid = 11 
RetryTimes = 5
SleepSeconds = 10 
#  --*---------------*--

#  --*--  ALARMS  --*--
alarms = {
    'default_alarms' : {
        'SEND'     :    [ 'value',    '>',    '0',   3], # alarm if value < 5000 & occured 3 times in succession
        'RECV'     :    [ 'value',    '>',    '0',   5],
        'RQUEUE'   :    [ 'queue_size',  '<=',    '0',  5],
        'SQUEUE'   :    [ 'queue_size',  '<',     '1',  7],
    },

    'runse_importer' : {
        'SEND'     :    [ 'value',    '<',    '1',   10], 
        'RECV'     :    [ 'value',    '<',    '1',    10],
        'RQUEUE'   :    [ 'queue_size',  '>',    '10000',  5],
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
        'SEND'     :    [ 'value',    '>',    '1',   1], 
        'RECV'     :    [ 'value',    '>',    '1',    1],
        'RQUEUE'   :    [ 'queue_size',  '<',    '10000',  5],
        'SQUEUE'   :    [ 'queue_size',  '<',    '10000',  5],
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
'12137577579520',
)

sparsepipelet = (
'12137577578496'
'12137577579008',
'12107512807936',
'12107512807424',
)
#  --*--------------*--

import httplib
import time
import os

HOSTNAME = os.popen('echo $HOSTNAME').read().split('.')[0];

pemap = {}

def main():
    alarmsleep = SleepSeconds
    retrycount = 0
    candi      = {}
    ret        = {}
    conn       = httplib.HTTPConnection(url['HOST'])
    conn.request('GET', url['PEMAP']+'appid='+str(appid))
    global pemap
    pemap      = dict(map(lambda x:x.split('|'), conn.getresponse().read().strip().split('\n')))
#    print pemap
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
                    # time:PEID:type(upstream PEID):value:retrycount    cq01-udw-dmf01==>Sun Dec 23 03:07:00 2012:5536212844800:SQUEUE():4:8 
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
        print 'MobileList:' + mobile
        mobilealarm = 'gsmsend -s tc-sys-monitor00.tc:15001 -s tc-sys-monitor01.tc:15001 *2*%s@"%s"' % (mobile, msg)
        os.system(mobilealarm)

def getalarms():
    conn              = httplib.HTTPConnection(url['HOST'])
    out               = {}
    for table in url['TABLES']:
        print url['TABLES']
        print '257----------'
#        conn.request('GET', table+'&limit=0,'+str(LookBackRows+1)+'&where=appid='+str(appid)+'%20and%20time%3E'+str(int(time.time())-LookBackSeconds))
        conn.request('GET','/log_metrics.php?do=view&view=QPS&show=txt&limit=0,1001&where=appid=11%20and%20time%3E1364983191')


#        print '%s' % (table+'&limit=0,'+str(LookBackRows+1)+'&where=appid='+str(appid)+'%20and%20time%3E'+str(int(time.time())-LookBackSeconds))
        print '259'
        data          = conn.getresponse().read().strip().split('\n')
        print '261'
        #print data
        title         = data.pop(0).split('|')
        print title
        data          = map(lambda x:x.split('|'), data)
        print '267'
        data.sort(key = lambda x:x[title.index('time')])
        print '269'
        print type(data)
        for line in data:
            print 'in for line in data'
            print type(line)
            items = dict(zip(title, line))
            print items
            print type(items)
            print items['PEID']
            print '271'
            uplen = 1
            print '273'
            if items.has_key('owners'):        
                uplen = max(uplen, len(items['owners'].split(',')) - 1)
                print '276'
            petype    = pemap[items['PEID']]
            print '278'
#            print 'items[PEID' + iterms['PEID']
            try:
                alarm = alarms[petype][items['type']]
                print '282'
            except:            
                if alarms['default_alarms'].has_key(items['type']):
                    alarm = alarms['default_alarms'][items['type']]
                else:
                    continue

            if eval(items[alarm[0]]+alarm[1]+alarm[2]+'*'+str(uplen)):
                out['%s:%s(%s)' % (items['PEID'], items['type'], items.get('owners', ''))] = \
                        [1, alarm[3], time.ctime(int(items['time'])), items[alarm[0]]]
        print 'func over!!!!!'
        
    return out
if __name__=='__main__':
    main()

