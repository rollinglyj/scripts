
import os
import sys


MYSQL_CMD_PREFIX='mysql -h10.46.104.60 -pMhxzKhl -P8357 -uroot -D offline'


def get_log_path(pa):
    MYSQL_CMD = MYSQL_CMD_PREFIX + ' -e "'+ "select l.name,s.path,v.version from TblLogVersionDef v inner join TblLogDef l on v.version=l.currentVersion and l.name='" + pa + "'and v.logDataid=l.dataid inner join TblDataStorage s on v.logDataVersionid=s.refid and s.refType=0;" +'"'+" | awk '{print $2}'" + " | tail -1 "
        
#    print MYSQL_CMD
    result = os.popen(MYSQL_CMD)
    for re in result:
        return re

def main():
    parameter = sys.argv
    for par in parameter[1:]:
        res   = get_log_path(par)
        print res
main()


