'''
Author: justinzhang
Email:  uestczhangchao@gmail.com/zhangchao08@baidu.com
Time: Thu Aug 22 11:45:06 CST 2013
'''
import os
import datetime
import common_data
import sys
from common_data import dag_list,HADOOP_CLIENT, MYSQL_QA, dict_slot_time,dict_map_input_bytes,yes_dict_slot_time,yes_dict_map_input_bytes,delta_slot_time,delta_map_input_bytes


def init_structure():
    for dag in dag_list:
        dict_slot_time[dag]           = 0;
        dict_map_input_bytes[dag]     = 0;
        yes_dict_slot_time[dag]       = 0;
        yes_dict_map_input_bytes[dag] = 0;
        delta_slot_time[dag]          = 0;
        delta_map_input_bytes[dag] = 0;


def get_slot_time(dag_name,base_time):
    
    time_format = base_time.split('-')
    year        = time_format[0]
    month       = time_format[1]
    day         = time_format[2]
    
    mkdate = datetime.date(int(year),int(month), int(day))

    yesterday = str(mkdate - datetime.timedelta(days = 1))
    yes = yesterday
    tomorrow  = str(mkdate + datetime.timedelta(days=1))
    yes_yes = str(mkdate - datetime.timedelta(days=2))
    print str(yesterday)+"--" + str(tomorrow) + "---" + str(yes_yes)

    yes_cmd = MYSQL_QA + 'select sum(mapinputbytes),sum(totalslottime) from TblDag td,TblJobComplete tj where td.jobid=tj.jobid and dagname=\''+ dag_name +'\' and partition>=\''+yesterday+' 00:00:00\' and partition<\''+ base_time +' 00:00:00\';"|tail -1|awk -F\'\\t\' \'{print $1,$2}\''

    cmd     = MYSQL_QA + 'select sum(mapinputbytes),sum(totalslottime) from TblDag td,TblJobComplete tj where td.jobid=tj.jobid and dagname=\''+ dag_name +'\' and partition>=\''+ base_time +' 00:00:00\' and partition<\''+ tomorrow +' 00:00:00\';"|tail -1|awk -F\'\\t\' \'{print $1,$2}\''

    #handle holmes
    if dag_name == 'udwetl_holmes4uap':
        yes_cmd = MYSQL_QA + 'select sum(mapinputbytes),sum(totalslottime) from TblDag td,TblJobComplete tj where td.jobid=tj.jobid and dagname=\''+ dag_name +'\' and partition>=\''+yes_yes+' 00:00:00\' and partition<\''+ yes +' 00:00:00\';"|tail -1|awk -F\'\\t\' \'{print $1,$2}\''
    
        cmd     = MYSQL_QA + 'select sum(mapinputbytes),sum(totalslottime) from TblDag td,TblJobComplete tj where td.jobid=tj.jobid and dagname=\''+ dag_name +'\' and partition>=\''+ yes +' 00:00:00\' and partition<\''+ base_time +' 00:00:00\';"|tail -1|awk -F\'\\t\' \'{print $1,$2}\''

    print yes_cmd
    print cmd
    result  = os.popen(cmd).readlines()
    results = result[0].split()
    print results[0] + "  " + results[1] + "-----"
    if results[1] != 'NULL':
        dict_slot_time[dag_name]=float(results[1])/(24*3600)
    if results[0]!='NULL':
        dict_map_input_bytes[dag_name]=float(results[0])/(1024*1024*1024)

    yes_result  = os.popen(yes_cmd).readlines()
    yes_results = yes_result[0].split()
    print yes_results[0] + "  " + yes_results[1] + "-----"
    if yes_results[1]!='NULL':
        yes_dict_slot_time[dag_name]       = float(yes_results[1])/(24*3600)
    if yes_results[0] != 'NULL':
        yes_dict_map_input_bytes[dag_name] = float(yes_results[0])/(1024*1024*1024)

    if yes_dict_slot_time[dag_name] != 0:
        delta_slot_time[dag_name] = (float(dict_slot_time[dag_name]) - float(yes_dict_slot_time[dag_name]))/(float(yes_dict_slot_time[dag_name]))
    if  yes_dict_map_input_bytes[dag_name] != 0 :
        delta_map_input_bytes[dag_name] = (float(dict_map_input_bytes[dag_name]) - float(yes_dict_map_input_bytes[dag_name]))/(float(yes_dict_map_input_bytes[dag_name]))

                                                                                                            
def print_dict():
    print "print slot_time"
    for dag in dag_list:
        print dag + ":" + str(dict_slot_time[dag])
    print "print map_input_bytes"
    for dag in dag_list:
        print dag + ":" + str(dict_map_input_bytes[dag])
    print 'yesterday ----- slot and mapinput data'

    print "yes_slot_time"
    for dag in dag_list:
        print dag + ":" + str(yes_dict_slot_time[dag])
    print "print yes_map_input_bytes"
    for dag in dag_list:
        print dag + ":" + str(yes_dict_map_input_bytes[dag])

    print "delta slot time and input_bytes"
    print "delta slot time"
    for dag in dag_list:
        print dag + ":" + str(delta_slot_time[dag])
    print "delta map input bytes"
    for dag in dag_list:
        print dag + ":" + str(delta_map_input_bytes[dag])

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

def mark_data(data):
    data[0]     = data[0]
    data[1]     = round(float(data[1]),1)
    data[2]     = mark_red_percent(data[2])
    data[3]     = round(float(data[3]),1)
    data[4]     = mark_red_percent(data[4])

    data[5]     = round(float(data[5]),1)
    data[6]     = mark_red_percent(data[6])

    data[7]  = round(float(data[7]),1)
    data[8]  = mark_red_percent(data[8])
    data[9]  = two_decimal_num(data[9])
    data[10] = two_decimal_num(data[10])
    data[11] = mark_map_log_size(data[11])

    data[12] = '<font color="red" size="5">'+three_decimal_num(data[12])+'</font>'
    data[13] = '<font color="green" size="5">'+three_decimal_num(data[13])+'</font>'
    data[14] = '<font color="green" size="5">'+three_decimal_num(data[14])+'</font>'
    return data

def mark_map_log_size(item):
    print str(item)+"******"
    item = float(two_decimal_num(float(item)))
    print item
    print type(item)
    if item<0.9 or item>1 :
        ret = "<font color=\"#FF0000\">" + two_decimal_num(item) + "</font><br>"
    else :
        ret = two_decimal_num(item)
    return ret
    
    
    
def mark_red_percent(item):
    tmp = round(float(item)*100,1)
    
    if tmp > 0:
        if tmp > 20:
            ret = "<font color=\"#FF0000\">+" + str(tmp) + "% </font><br>"
        else:
            ret = "+" + str(tmp) + "%"
    elif tmp < 0:
        if abs(tmp) > 20:
            ret = "<font color=\"#FF0000\">" + str(tmp) + "% </font><br>"
        else:
            ret = str(tmp)+"%"
    else :
        return '0.0%'
    
    return ret

def data_to_str(data):
    for i in range(len(data)):
        data[i] = str(data[i])
    return data

def one_decimal_num(float_number):
    return '{0:.1f}'.format(float(float_number))
    
def two_decimal_num(float_number):
    return '{0:.2f}'.format(float(float_number))

def three_decimal_num(float_number):
    return '{0:.3f}'.format(float(float_number))

        
if (__name__=='__main__'):
#    re = get_cmd_result(0,'xxx');
#    re  = path_exit(HADOOP_CLIENT, '/apx/')
#    print re;

#    ret = get_per_path_size(HADOOP_CLIENT,'/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event/event_action=baidustat4uap_event/event_day=2013081')
#    print ret
#    print type(ret)
#    ret = analysis_Dag('3','sobar')
#    print ret
#    init_structure()
    
#    for dag in dag_list:
#        get_slot_time(dag,sys.argv[1])
#    print_dict()
    data        = ['sobar', '173.01', '0.34114018051', '163.029934491', '-0.33705093567', '28.55', '-0.382034632035', '6.22532407407', '-0.177830836159', '27.7913242654', '0.165019363043', '0.942315094451']
#    ret        = mark_data(data)
#    ret2       = mark_map_log_size(94555)
#    print ret2
    ret_decimal = two_decimal_num(1.6)
    ret_map_log = mark_map_log_size(0.9)
    print type(ret_map_log)
    print ret_map_log
    print three_decimal_num(1)

     
