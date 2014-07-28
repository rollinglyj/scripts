from sgsCrawler import *

if __name__=='__main__':
    if(len(sys.argv) == 3):
        if(sys.argv[1] == '-n'):
            etlToDB(sys.argv[2])
        elif(sys.argv[1] == '-d'):
            displayInfo(sys.argv[2])
        else:
            print "Usage: python main.py <-n>|<-d> <corpname>|<recordNum> "
    else:
        print "Erro usage!"
