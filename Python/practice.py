import sys;


dict1 = {"id":11}
print dict1["id"]



print type(dict1)


dtest = r'{"id":11}'


keys   = ('name', 'age', 'food')
values = ('Monty', 42, 'spam')

dict = {}
junk = map(lambda k, v: dict.update({k : v}),keys, values)
print dict

revf        = {}
revf['abc'] = 'def'
print revf

#rev_ref = dict((v,k) for k,v in revf.iteritems())
#print rev_ref

f = lambda x: x**2 + 2*x -5
mult3 = filter(lambda x: x %3 == 0 , [1,2,3,4,5,6,7,8,9])
print mult3

mult_3 = [x for x in [1,2,3,4,5,6,7,8,9] if x%3==0]
print mult_3


print '******2013-4-2*********'
sys.path.append('../')
sys.path.append('../manager/server')

x = 1
print eval('x+1')


input_source = eval("[[u'map_mmproxy_log_backtrace', u'hdfs://szwg-ston-hdfs.dmop.baidu.com:54310///log/1630/map_mmproxy_log/20130317//0000']]")


input_info = input_source[0]
print str(input_info) + "fdsf"
print input_info[0]
print input_info[1]





