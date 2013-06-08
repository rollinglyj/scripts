print "hello"
alist = [(100,2),(3,4)]
#print alist
#print zip(*alist)

print map(max, zip(*alist))
