from sgsCrawler import *

if __name__=='__main__':
    if(len(sys.argv) == 3):
        if(sys.argv[1] == '-n'):
            etlToDB(sys.argv[2])
        else:
            print "Erro usage!"
    else:
        print "Erro usage!"
