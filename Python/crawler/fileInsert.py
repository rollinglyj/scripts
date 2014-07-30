
#!/usr/bin/python
#-*-coding:utf-8-*-
import sys
from sgsCrawler import *
reload(sys)
sys.setdefaultencoding('utf-8')

def fromFileCrawl():
    f = open("dbList1.file", "r")
    for name in f:
        print name
        etlToDB(name)
    f.close()

if __name__ == '__main__':
    fromFileCrawl()




