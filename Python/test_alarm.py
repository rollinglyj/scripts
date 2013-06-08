import sys;
import os;
import httplib;
import time;


HOSTNAME = os.popen('echo $HOSTNAME').read().split('.')[0]
print HOSTNAME


#  --*-- URL --*--
url      = {
        'HOST'    :    'db-dstream-online.dmop.baidu.com:8008',
            'PEMAP'      :    '/api_app_pe.php?',
            'TABLES'   :   [
                '/log_metrics.php?do=view&view=QPS&show=txt', # QPS
                        '/log_metrics.php?do=view&view=QWatcher&show=txt', #Queue size
                    ]
        }
#  --*-------------*--

#  --*-- PARAMETER --*--
LookBackSeconds = 15
LookBackRows    = 1000
appid           = 11
RetryTimes      = 5
SleepSeconds    = 10
#  --*---------------*--  

#  --*-- PARAMETER --*--
LookBackSeconds = 15
LookBackRows    = 1000
appid           = 11
RetryTimes      = 5
SleepSeconds    = 10
#  --*---------------*--  

conn = httplib.HTTPConnection(url['HOST']);
conn.request('GET',url['PEMAP']+'appid='+str(appid))

global pemap
pemap = dict(map(lambda x:x.split('|'), conn.getresponse().read().strip().split('\n')))
#print pemap

for table in url['TABLES']:
    print table
    


#print '*************%s' %(conn.getresponse().read().strip().split('\n'))




