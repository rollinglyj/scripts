'''
Author: justinzhang
Email:  uestczhangchao@gmail.com
Time: Thu Aug 22 11:45:06 CST 2013
'''
import os
HADOOP_CLIENT = "~/Tool/hadoop-ecomon/bin/hadoop"

def get_cmd_result(opt, cmd):
    if (opt==0):
        cmd = cmd + '>/dev/null 2>&1; echo $?';
        re  = os.popen(cmd).readlines();
        re  = re[0].strip();
        return re;
    else:
        re  = os.popen(cmd).readlines();
        re  = re[0].strip();
        return re


def path_exit(HADOOP_CLIENT, path):
    cmd     = HADOOP_CLIENT + ' fs -test -e ' + path;
    re      = get_cmd_result(0,cmd)
    return re

        
def get_per_path_size(HADOOP_CLIENT, path):
    cmd        = HADOOP_CLIENT + ' fs -dus ' + path + " | awk '{print $2}'"
    if path_exit(HADOOP_CLIENT, path)=='0':
        print "Path EXIT: " +path + "|| CMD ID:-->" + cmd
        result = os.popen(cmd).readlines()
        return result[0].strip()
    else :
        print "Path Not EXIT! : " + path +"|| CMD IS: " + cmd
        return -1


def analysis_Dag(opt,dagname):
    MYSQL_CMD_PREFIX = 'mysql -h10.46.104.60 -pMhxzKhl -P8357 -uroot -D offline'
    dag = dagname
    
    DAG_CMD1 = MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\".*log\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''


    DAG_CMD2 =MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\"event\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''


    DAG_CMD3 =  MYSQL_CMD_PREFIX + ' -e "' + 'select content from TblETLDagVersionDef where jobid = (select jobid from TblETLDagDef where name=\''+dag+'\')\G;"'+'| cat | grep "type=\\"big_event\\"" | awk \'{print $2}\' | awk -F\'=\' \'{print $2}\'|awk -F\'\"\' \'{print $2}\''
    if(opt=='1'):
        result = os.popen(DAG_CMD1).readlines()
        return result
    elif(opt=='2'):
        result = os.popen(DAG_CMD2).readlines()
        return result

    elif(opt=='3'):
        result = os.popen(DAG_CMD3).readlines()
        return result
        
        
if (__name__=='__main__'):
#    re = get_cmd_result(0,'xxx');
#    re  = path_exit(HADOOP_CLIENT, '/apx/')
#    print re;

#    ret = get_per_path_size(HADOOP_CLIENT,'/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event/event_action=baidustat4uap_event/event_day=2013081')
#    print ret
#    print type(ret)
    ret  = analysis_Dag('3','sobar')
    print ret
    
