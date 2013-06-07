#!/usr/bin/env python

def displayNumType(num):
    print num, 'is',
    if isinstance(num, (int, long, float, complex)):
        print 'a number of type:', type(num).__name__
    else:
        print 'not a number at all!!'
displayNumType(-69)
displayNumType(9999999999999)
displayNumType(98.6)
displayNumType(-5.2+1.9)
displayNumType('xxx')
sStr1 = 'cpro_pb_2012-05-24T15:00:00_32910_ver23'
sStr2 = '_2012'
index = sStr1.find(sStr2)
print index
print sStr1[0:sStr1.find('_2012')]
