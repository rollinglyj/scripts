import sys
import os
import time
import datetime
import MailClient
from common_data import HADOOP_CLIENT,dag_list,dag_input_dict,dag_log_dict,dag_output_dict,input_size_dict,output_size_dict, yes_input_size_dict,yes_output_size_dict,delta_input_size_dict,delta_output_size_dict,dict_map_input_bytes,dict_slot_time,delta_slot_time,delta_map_input_bytes
import common_lib
from common_lib import get_slot_time,init_structure,print_dict

day_time      = time.strftime('%Y%m%d',time.localtime(time.time()))
print "today is :"+str(day_time)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
#print yesterday
yes       = (str(yesterday))[0:10]
yes = yes.replace('-','')

print "yesterday is:"+str(yes)

def get_output_report(base_time):

    time_format = base_time.split('-')
    year        = time_format[0]
    month       = time_format[1]
    day         = time_format[2]
    
    mkdate = datetime.date(int(year),int(month), int(day))

    yesterday = str(mkdate - datetime.timedelta(days = 1))
    tomorrow  = str(mkdate + datetime.timedelta(days=1))

    yes = yesterday.replace('-','')
    day_time = tomorrow.replace('-','')
    
    #print str(yes)+"--" + str(day_time)

    
#    print "start_time " + str(start_time)
#    print "end_time" + str(end_time)
    for dag in dag_list:
        output_size_dict[dag]       = 0
        yes_output_size_dict[dag]   = 0
        delta_output_size_dict[dag] = 0
        
    
    for dag in dag_list:
        log_path       = dag_output_dict[dag]
        for log in log_path:
            ls_cmd     = HADOOP_CLIENT+" fs -ls "+log.strip()+ "/event_day=" + day_time +'>exit_file 2>&1;cat exit_file|grep "No such file or directory"'
            yes_ls_cmd = HADOOP_CLIENT+" fs -ls "+log.strip()+ "/event_day=" + yes +'>exit_file 2>&1;cat exit_file|grep "No such file or directory"'
            print "current yes command is :" + str(yes_ls_cmd)
            print "current command is :" + str(ls_cmd)
            ls_cmd_re  = os.popen(ls_cmd).readlines()
            
            if ls_cmd_re:
                print "In "+dag+ " " + str(log)+" not exist "
                ls_cmd_re                = []
            else:
                print "In "+dag+ " " + str(log)+"  exist "
                ls_cmd_re                = []
                get_size_cmd             = HADOOP_CLIENT + " fs -dus " + log.strip() + "/event_day=" + day_time + " | awk '{print $2}'"
                print get_size_cmd
                get_size_cmd_re          = os.popen(get_size_cmd).readlines()
                print type(get_size_cmd_re)
                log_size                 = str(get_size_cmd_re[0])
                print  type(log_size)
                log_size                 = str(log_size).replace('\n','')
                print log_size
                ToGB                     = float(log_size)/(1024*1024*1024)
                ToGB                     = round(ToGB,2)
                print "current :" + str(ToGB) + "GB"
                if output_size_dict.has_key(dag):
                    output_size_dict[dag] = output_size_dict[dag] + ToGB
                    print str(dag) + " Total size :" + str(output_size_dict[dag]) + "--second time"
                else:
                    output_size_dict[dag] = ToGB
                    print str(dag) + " Total size : " + str(output_size_dict[dag]) + "--first time"

            yes_ls_cmd_re                     = os.popen(yes_ls_cmd).readlines()
            if yes_ls_cmd_re:
                print "In "+dag+ " " + str(log)+" not exist "
                yes_ls_cmd_re                 = []
            else:
                print "In "+dag+ " " + str(log)+"  exist "
                yes_ls_cmd_re                 = []
                get_size_cmd                  = HADOOP_CLIENT + " fs -dus " + log.strip() + "/event_day=" + yes + " | awk '{print $2}'"
                print get_size_cmd
                get_size_cmd_re               = os.popen(get_size_cmd).readlines()
                print type(get_size_cmd_re)
                log_size                      = str(get_size_cmd_re[0])
                print  type(log_size)
                log_size                      = str(log_size).replace('\n','')
                print log_size
                ToGB                          = float(log_size)/(1024*1024*1024)
                ToGB                          = round(ToGB,2)
                print "current " + str(ToGB) + "GB"
                if yes_output_size_dict.has_key(dag):
                    yes_output_size_dict[dag] = yes_output_size_dict[dag] + ToGB
                    print str(dag) + " Total size :" + str(yes_output_size_dict[dag]) + "--second time"
                else:
                    yes_output_size_dict[dag] = ToGB
                    print str(dag) + " Total size : " + str(yes_ouput_size_dict[dag]) + "--first time"

    timestamp = str(time.strftime('%Y%m%d%H%M%S',time.localtime(time.time())));
    timestamp = ''
    file_obj_output                           = open("output_log_size_"+ timestamp+".txt",'w')
    yes_file_obj_output = open("yes_output_log_size_"+ timestamp +".txt",'w');
    file_obj_output_delta                     = open("delta_output_size_" + timestamp +".txt",'w')
    file_obj_output.write(day_time)
    file_obj_output.write('\n')
    
    for key in dag_list:
        file_obj_output.write(key)
        file_obj_output.write('\t')
        file_obj_output.write(str(output_size_dict[key]))
        file_obj_output.write('\n')
        file_obj_output_delta.write(key)
        file_obj_output_delta.write('\t')
        if yes_output_size_dict[key]!=0:
            huanbi = float(output_size_dict[key]-yes_output_size_dict[key])/yes_output_size_dict[key]
            huanbi = huanbi*100.00
            print ("%.2f" % huanbi)
            huanbi = str(huanbi)+"%"
        else:
            huanbi = 0
        file_obj_output_delta.write(str(huanbi))
        file_obj_output_delta.write('\n')
        yes_file_obj_output.write(key);
        yes_file_obj_output.write('\t')
        yes_file_obj_output.write(str(yes_output_size_dict[key]))
        yes_file_obj_output.write('\n')
    
    file_obj_output.close()
    yes_file_obj_output.close()
    file_obj_output.close()
    file_obj_output_delta.close()
                        


def get_input_report(base_time):


    time_format = base_time.split('-')
    year        = time_format[0]
    month       = time_format[1]
    day         = time_format[2]
    
    mkdate = datetime.date(int(year),int(month), int(day))

    yesterday = str(mkdate - datetime.timedelta(days = 1))
    tomorrow  = str(mkdate + datetime.timedelta(days=1))

    yes = yesterday.replace('-','')
    day_time = tomorrow.replace('-','')
            
#get input log size
    for dag in dag_list:
        input_size_dict[dag]       = 0
        delta_input_size_dict[dag] = 0
        yes_input_size_dict[dag]   = 0

    for dag in dag_list:
        print "Current Dag is:" + str(dag)
        log_path       = dag_input_dict[dag]
        for log in log_path:
            print str(dag)+":"+str(log)
            ls_cmd     = HADOOP_CLIENT+" fs -ls "+log.strip()+ "/" + day_time +'>exit_file 2>&1;cat exit_file|grep "No such file or directory"'
            yes_ls_cmd = HADOOP_CLIENT+" fs -ls "+log.strip()+ "/" + yes +'>exit_file 2>&1;cat exit_file|grep "No such file or directory"'
            print "current yes command is :" + str(yes_ls_cmd)
            print "curren command is :" + str(ls_cmd)
            ls_cmd_re  = os.popen(ls_cmd).readlines()
            
            if ls_cmd_re:
                print "In "+dag+ " " + str(log)+" not exist "
                ls_cmd_re                = []
            else:
                print "In "+dag+ " " + str(log)+"  exist "
                ls_cmd_re                = []
                get_size_cmd             = HADOOP_CLIENT + " fs -dus " + log.strip() + "/" + day_time + " | awk '{print $2}'"
                print get_size_cmd
                get_size_cmd_re          = os.popen(get_size_cmd).readlines()
                print type(get_size_cmd_re)
                log_size                 = str(get_size_cmd_re[0])
                print  type(log_size)
                log_size                 = str(log_size).replace('\n','')
                print log_size
                ToGB                     = float(log_size)/(1024*1024*1024)
                ToGB                     = round(ToGB,2)
                print str(ToGB) + "GB"
                if input_size_dict.has_key(dag):
                    input_size_dict[dag] = input_size_dict[dag] + ToGB
                    print str(dag) + "size :" + str(input_size_dict[dag]) + "--second time"
                else:
                    input_size_dict[dag] = ToGB
                    print str(dag) + " size : " + str(input_size_dict[dag]) + "--first time"

            yes_ls_cmd_re                    = os.popen(yes_ls_cmd).readlines()
            if yes_ls_cmd_re:
                print "In "+dag+ " " + str(log)+" not exist "
                yes_ls_cmd_re                = []
            else:
                print "In "+dag+ " " + str(log)+"  exist "
                yes_ls_cmd_re                = []
                get_size_cmd                 = HADOOP_CLIENT + " fs -dus " + log.strip() + "/" + yes + " | awk '{print $2}'"
                print get_size_cmd
                get_size_cmd_re              = os.popen(get_size_cmd).readlines()
                print type(get_size_cmd_re)
                log_size                     = str(get_size_cmd_re[0])
                print  type(log_size)
                log_size                     = str(log_size).replace('\n','')
                print log_size
                ToGB                         = float(log_size)/(1024*1024*1024)
                ToGB                         = round(ToGB,2)
                print str(ToGB) + "GB"
                if yes_input_size_dict.has_key(dag):
                    yes_input_size_dict[dag] = yes_input_size_dict[dag] + ToGB
                    print str(dag) + "size :" + str(yes_input_size_dict[dag]) + "--second time"
                else:
                    yes_input_size_dict[dag] = ToGB
                    print str(dag) + " size : " + str(yes_input_size_dict[dag]) + "--first time"
    file_obj_input                           = open("input_log_size.txt",'w')
    yes_file_obj_input = open("yes_input_log_size.txt",'w');
    file_obj_input_delta                     = open("delta_input_size.txt",'w')
    file_obj_input.write(day_time)
    file_obj_input.write('\n')
    
    for key in dag_list:
        file_obj_input.write(key)
        file_obj_input.write('\t')
        file_obj_input.write(str(input_size_dict[key]))
        file_obj_input.write('\n')
        file_obj_input_delta.write(key)
        file_obj_input_delta.write('\t')
        if yes_input_size_dict[key]!=0:
            huanbi = float(input_size_dict[key]-yes_input_size_dict[key])/yes_input_size_dict[key]
            huanbi = huanbi*100.00
            print ("%.2f" % huanbi)
            huanbi = str(huanbi)+"%"
        else:
            huanbi = 0
        file_obj_input_delta.write(str(huanbi))
        file_obj_input_delta.write('\n')
        yes_file_obj_input.write(key);
        yes_file_obj_input.write('\t')
        yes_file_obj_input.write(str(yes_input_size_dict[key]))
        yes_file_obj_input.write('\n')
    
    file_obj_input.close()
    yes_file_obj_input.close()
    file_obj_input_delta.close()
    
if __name__=='__main__':

    init_structure()
    for dag in dag_list:
        get_slot_time(dag,sys.argv[1])
    print_dict()

    if len(sys.argv)==2:
        get_input_report(sys.argv[1])
        get_output_report(sys.argv[1])
    else:
        get_input_report('2013-08-25')
        get_output_report('2013-08-24')

    
    mailclient   = MailClient.MailClient()

    title        = 'uap-resource-'
    from_email   = 'zhangchao08@baidu.com'
    to_email     = 'zhangchao08@baidu.com'
    template_id  = '24'

    for dag in dag_list:
        data[0]      = str(dag)
        data[1]      = str(input_size_dict[dag])
        data[2]      = str(delta_input_size_dict[dag])
        data[3]      = str(dict_map_input_bytes[dag])
        data[4]      = str(delta_map_input_bytes[dag])
        data[5]      = str(output_size_dict[dag])
        data[6]      = str(delta_output_size_dict[dag])
        data[7]      = str(dict_slot_time[dag])
        data[8]      = str(delta_slot_time[dag])

        if dict_slot_time[dag] != 0:
            data[9]  = str(float(input_size_dict[dag])/dict_slot_time[dag])
        else :
            data[9]  = '0'

        if input_size_dict[dag] != 0 :
            data[10] = str(float(output_size_dict[dag])/float(input_size_dict[dag]))
        else:
            data[10] = '0'
        
        if input_size_dict[dag] != 0:
            data[11] = str(float(dict_map_input_bytes[dat])/float(input_size_dict[dag]))
        else:
            data[11] = '0'
        mailclient.sendBanch(from_email, to_email,title,data,"list",template_id)
        
        
