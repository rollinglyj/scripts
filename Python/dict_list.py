import json
import time
import os

#s = json.loads('{"applicat_explorer":{"channel":0,"peid":12345,"value":123}}')
#s = json.loads('{"lbs":{"channel":3,"peid":323,"value":23223}}')
#print s

pe_list = []
for i in range(0,12):
    pe_list.append(i)
for peid in pe_list:
    print peid
print time.time()


items = eval('{"PEID": "12163347387648", "ip": "10.50.39.61", "time": "1364983200", "value": "0", "APPID": "11", "type": "SEND"}')
print items
print items['PEID']
print type(items)

