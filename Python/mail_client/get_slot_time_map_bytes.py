import sys
import os
import time
import datetime
dict_slot_time           = {}
dict_map_input_bytes     = {}
yes_dict_slot_time       = {}
yes_dict_map_input_bytes = {}

file_object=open('slot_time.txt','w')
file_object2=open('map_input_bytes.txt','w')
def execute():
    day_time=time.strftime('%Y-%m-%d',time.localtime(time.time()))
#    day_time=time.strftime('%Y%m%d')
    print day_time
    yesterday=datetime.datetime.now() - datetime.timedelta(days=1)
    yes=(str(yesterday))[0:10]
    print yes
    day_time='2013-08-20'
    yes='2013-08-19'

#    dag_list=["udwetl_baidustat4uap","dag_baike","udwetl_bdclk4uap","columbus_ad_display","udwetl_fc_dorado","dag_hao123click","udwetl_houyi4uap","udwetl_holmes4uap","nova_ad_display","ps_click_union","ps_query_online","wise_ps_click_display_5","sobar"]
    dag_list=["nova_ad_display","columbus_ad_display","ps_query_online","wise_ps_click_display_5","udwetl_baidustat4uap","udwetl_houyi4uap","ps_click_union","dag_baike","dag_hao123click","sobar","udwetl_fc_dorado","udwetl_bdclk4uap","udwetl_holmes4uap"]

    for dag in dag_list:
        cmd="mysql -h10.216.121.31 -uroot -pMhxzKhl -D udwbenchmark -e "+'"select sum(mapinputhdfs),sum(totalslottime) from TblDag td,TblJobComplete tj where td.jobid=tj.jobid and dagname=\''+dag+'\' and partition>=\''+yes+' 00:00:00\' and partition<\''+ day_time+' 00:00:00\';"|tail -1|awk -F\'\\t\' \'{print $1,$2}\''

        print cmd
        result = os.popen(cmd).readlines()
        results=result[0].split()
        dict_slot_time[dag]=float(results[1])/(24*3600)
        dict_map_input_bytes[dag]=float(results[0])/(1024*1024*1024)

    for key in dag_list:
        file_object.write(key)
        file_object.write('\t')
        file_object.write(str(dict_slot_time[key]))
        file_object.write('\n')
    file_object.close()
    for key in dag_list:
        file_object2.write(key)
        file_object2.write('\t')
        file_object2.write(str(dict_map_input_bytes[key]))
        file_object2.write('\n')
    file_object2.close()
execute()    
