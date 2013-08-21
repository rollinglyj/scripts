import sys
import os

MYSQL_CMD_PREFIX = 'mysql -h10.46.104.60 -pMhxzKhl -P8357 -uroot -D offline'

def analysis_Dag(opt,dagname):
    dag = dagname
    
    DAG_CMD1 = MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\".*log\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''


    DAG_CMD2 =MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\"event\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''


    DAG_CMD3 =  MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\"big_event\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''
    if(opt=='1'):
        result = os.popen(DAG_CMD1)
        for re in result:
            print re
    elif(opt=='2'):
        result = os.popen(DAG_CMD2)
        for re in result:
            print re        

    elif(opt=='3'):
        result = os.popen(DAG_CMD3)
        for re in result:
            print re        
            
def main():
#    print '\n 1:get_log_name\n 2:get_event_name\n 3:get_big_evnet_name\n'
    re = analysis_Dag(sys.argv[1],sys.argv[2])

main()


