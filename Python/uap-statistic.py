import sys
import os
import time
import datetime

HADOOP_CLIENT="~/Tool/hadoop-ecomon/bin/hadoop"

'''dag_list=["udwetl_baidustat4uap","dag_baike","udwetl_bdclk4uap","columbus_ad_display","udwetl_fc_dorado","dag_hao123click","udwetl_houyi4uap","udwetl_holmes4uap","nova_ad_display","ps_click_union","ps_query_online","wise_ps_click_display_5","sobar"]

dag_input_dict = {
                "udwetl_baidustat4uap":['/log/11523/baidustat_holmes_session_et2'],
                "dag_baike":['/log/100025586/baike_nginx_access_2ecomon'],
                "udwetl_bdclk4uap":['/log/11523/doris_log_dcharge_bd_cmon_ecomon'],
                "columbus_ad_display":['/log/11523/cbrank_kun_ecomon','/log/30929/pfs_tpf_log_udw_on'],
                "udwetl_fc_dorado":['/log/30929/dr_dorado_udw_on'],
                "dag_hao123click":['/app/bigpipe/MCO/CLOUD/HAO123/hao123_nsclick_log/bae-hao123-nsclick-pipe'],
                "udwetl_houyi4uap":['/app/bigpipe/ECOM/houyi/hy_ck_apache_log/ecom-houyi-click-apache-pipe/'],
                "udwetl_holmes4uap":['/log/11523/cm_da_nova_holmes_basic_ecomon'],
                "nova_ad_display":['/log/30929/ecom_pb_cpro_nor_udw_on','/log/30929/ecom_pb_cpro_abnor_udw_on','/app/bigpipe/ECOM/nova/feature_for_fc/nova-pfs-feature-fc-pipe'],
                "ps_click_union":['/app/bigpipe/PS/www/online/unclk/ps-unionclick-pipe','/app/bigpipe/PS/www/online/psclk/ps-clicklog-pipe'],
                "ps_query_online":['/app/bigpipe/PS/www/online/unclk/ps-unionclick-pipe','/app/bigpipe/PS/www/online/psclk/ps-clicklog-pipe','/app/ns/udw/remora/bws-second/output/nor','/app/ns/udw/remora/bws-second/output/abnor','/app/bigpipe/PS/www/online/ps-bz/ps-bzlog-pipe'],
                "wise_ps_click_display_5":['/app/bigpipe/MCO/MI/wise-tc2-front/wise-tc2-front-pipe','/app/bigpipe/MCO/MI/wise_phpui_show/wise-show-pui-pipe','/log/30929/wise_remora_show_udw_on'],
                "sobar":['/app/bigpipe/CLIENT/BAR/sboar_urldata/sobar-urldata-pipe']
}

dag_log_dict = {

               "udwetl_baidustat4uap":['baidustat_holmes_session_et2'],
                "dag_baike":['baike_nginx_access_2ecomon'],
                "udwetl_bdclk4uap":['doris_log_dcharge_bd_cmon_ecomon'],
                "columbus_ad_display":['cbrank_kun_ecomon','pfs_tpf_log_udw_on'],
                "udwetl_fc_dorado":['dr_dorado_udw_on'],
                "dag_hao123click":['hao123_nsclick_log'],
                "udwetl_houyi4uap":['hy_ck_apache_log'],
                "udwetl_holmes4uap":['cm_da_nova_holmes_basic_ecomon'],
                "nova_ad_display":['ecom_pb_cpro_nor_udw_on','ecom_pb_cpro_abnor_udw_on','feature_for_fc'],
                "ps_click_union":['union_click_accesslog','click'],
                "ps_query_online":['union_click_accesslog','click','bws_nor','bws_abnor','bz'],
                "wise_ps_click_display_5":['tc2_front','wise_phpui_show','wise_remora_show_udw_on'],
                "sobar":['sobar']
}

dag_output_dict = {
                "udwetl_baidustat4uap":['/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event'],
                "dag_baike":[],
                "udwetl_bdclk4uap":['/app/ns/udw/release/warehouse/udwetl_bdclk4uap_event'],
                "columbus_ad_display":[],
                "udwetl_fc_dorado":['/app/ns/udw/release/warehouse/udwetl_fcadclick_2'],
                "dag_hao123click":[],
                "udwetl_houyi4uap":['/app/ns/udw/release/warehouse/udwetl_houyi4uap_event'],
                "udwetl_holmes4uap":['/app/ns/udw/release/warehouse/'],
                "nova_ad_display":[],
                "ps_click_union":[],
                "ps_query_online":[],
                "wise_ps_click_display_5":[],
                "sobar":['/app/ns/udw/release/warehouse/udwetl_sobarurldata']
}
'''

dag_list=["udwetl_baidustat4uap",]
dag_input_dict = {"udwetl_baidustat4uap":['/log/11523/baidustat_holmes_session_et2'], }
dag_output_dict = {"udwetl_baidustat4uap":['/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event'], }

input_size_dict           = {}
output_size_dict          = {}
yes_input_size_dict = {}
yes_output_size_dict = {}
delta_input_size_dict={}

day_time      = time.strftime('%Y%m%d',time.localtime(time.time()))
print "today is :"+str(day_time)

yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
#print yesterday
yes       = (str(yesterday))[0:10]
yes = yes.replace('-','')

print "yesterday is:"+str(yes)


def uap_report():
    cmd                       = HADOOP_CLIENT+' fs -ls /'
   # result                   = os.popen(cmd).readlines()
    result                    = []
    for re in result:
        print re
#get input log size
    for dag in dag_list:
        input_size_dict[dag]  = 0
        output_size_dict[dag] = 0
        delta_input_size_dict = 0
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
    file_obj_output                          = open("output_size.txt",'w')
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
        huanbi = float(input_size_dict[key]-yes_input_size_dict[key])/yes_input_size_dict[key]
        print huanbi
        huanbi = round(huanbi*100,3)
        huanbi = str(huanbi)+'%'
        file_obj_input_delta.write(huanbi)
        file_obj_input_delta.write('\n')
    
    file_obj_input.close()
    file_obj_output.close()
    file_obj_input_delta.close()
    

uap_report()
