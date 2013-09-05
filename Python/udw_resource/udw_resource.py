import os
import sys
MYSQL_DC='mysql -h10.220.156.34 -udc_user -pdc_user -P3306 -D SZWG_ECOMON -e "'
MYSQL_STON = 'mysql -h10.220.156.34 -udc_user -pdc_user -P3306 -D SZWG_STON -e "'
HADOOP_CLIENT = "~/Tool/hadoop-ecomon/bin/hadoop"

'''lbs_log_path = ['/app/bigpipe/NS/map/apimap-lighttpd_log/ns-map-apimap-lighttpd-pipe','/app/bigpipe/NS/map/apimap_log/ns-map-apimap-pipe','/app/bigpipe/NS/map/api_lighttpd_log/ns-map-apilighttpdlog-pipe','/app/bigpipe/NS/map/locationmap_log/ns-map-locationmap-pipe','/app/bigpipe/NS/map/mapbasic_log/ns-map-mapbasic-pipe','/app/bigpipe/NS/map/mmproxy-client_log/ns-map-mmproxy-client-pipe','/app/bigpipe/NS/map/mobilemap_log/ns-map-mobilemap-pipe','/app/bigpipe/NS/map/wapmap-lighttpd_log/ns-map-wapmap-lighttpd-pipe','/app/bigpipe/NS/map/wapmap_log/ns-map-wapmap-pipe','/app/bigpipe/NS/map/webmap-lighttpd_log/ns-map-webmap-lighttpd-pipe','/app/bigpipe/NS/map/webmap_log/ns-map-webmap-pipe','/log/100025758/lbc_inf_log','/log/30929/floashre_lighttpd','/log/30929/v1_map_iphone_udw','/log/30929/v2_map_android_udw']

ps_log_path = ['/app/bigpipe/PS/www/online/inter-psclk/gps-click-access-pipe','/app/bigpipe/PS/www/online/ps-bz/ps-bzlog-pipe','/app/bigpipe/PS/www/online/psclk/ps-clicklog-pipe','/app/bigpipe/PS/www/online/snap-apache/snapshot-apache-pipe','/app/bigpipe/PS/www/online/unclk/ps-unionclick-pipe','/app/ns/udw/bigpipe/union-pipe/','/app/ns/udw/log/bws_abnor_udw_on_backtrace','/app/ns/udw/log/bws_udw_on_backtrace/','/app/ns/udw/remora/bws-second/output/abnor','/app/ns/udw/remora/bws-second/output/nor','/log/100025586/gps_bws_udw_ecomon','/log/100025586/gps_bz_udw_ecomon','/log/30929/bws_abnor_udw_on','/log/30929/bws_abnor_udw_on/','/log/30929/bws_udw_on','/log/30929/bws_udw_on/','/log/30929/click_acces_udw_on','/log/30929/click_acces_udw_on/','/log/30929/ip_dim_udw_on','/log/30929/ip_tn_dim_udw_on','/log/30929/ps_bz_log_udw_on','/log/30929/ps_bz_log_udw_on/','/log/30929/ps_tn_dim_udw_on','/log/30929/spamcookie_day','/log/30929/spamcookie_hour','/log/30929/spamip_hour']



wise_log_path = ['/app/bigpipe/1130/phpui_searchbox','/app/bigpipe/1130/phpui_searchbox/log','/app/bigpipe/1130/wise_pcsuite','/app/bigpipe/MCO/MI/wise-explore/mco-wise-explore-pipe','/app/bigpipe/MCO/MI/wise-open-log/mco-wise-open-log-pipe','/app/bigpipe/MCO/MI/wise-phpui-searchbox/wise-phpui-searchbox-pipe','/app/bigpipe/MCO/MI/wise-phpui-sug/mco-wise-phpui-sug-pipe','/app/bigpipe/MCO/MI/wise-phpuisearch/wise-phpuisearch-pipe','/app/bigpipe/MCO/MI/wise-tc2-front/wise-tc2-front-pipe','/app/bigpipe/MCO/MI/wise_index_new/wise-indexnew-pipe','/app/bigpipe/MCO/MI/wise_phpui_show/wise-show-pui-pipe','/app/ns/udw/log/activeuser_udwps_backtrace','/app/ns/udw/log/api_lighttpd_log_backtrace','/app/ns/udw/log/armor_ubc_install_info_udw_on_backtrace','/app/ns/udw/log/armor_ubc_keep_alive_udw_on_backtrace','/app/ns/udw/log/armor_ubc_op_app_info_udw_on_backtrace','/app/ns/udw/log/armor_ubc_op_num_udw_on_backtrace','/app/ns/udw/log/armor_ubc_op_single_str_udw_on_backtrace','/app/ns/udw/log/bd-input-skin_backtrace','/app/ns/udw/log/bd-input-userinfo_backtrace','/app/ns/udw/log/bd-input_backtrace','/app/ns/udw/log/browser_criticaltech_udw_backtrace','/app/ns/udw/log/browser_general_udw_backtrace','/app/ns/udw/log/browser_openweb_udw_backtrace','/app/ns/udw/log/browser_useraction_udw_backtrace','/app/ns/udw/log/bws_abnor_udw_on_backtrace','/app/ns/udw/log/bws_udw_on_backtrace','/app/ns/udw/log/chunlei_ubc_ubcdata_log_backtrace','/app/ns/udw/log/client_update_udw_backtrace','/app/ns/udw/log/day_inputsort_udw_backtrace','/app/ns/udw/log/day_unsetup_udw_backtrace','/app/ns/udw/log/dingwei_loc1_backtrace','/app/ns/udw/log/floashre_lighttpd_backtrace','/app/ns/udw/log/fm_lighttpd_backtrace','/app/ns/udw/log/ime_commitword_log_udw_backtrace','/app/ns/udw/log/ime_liveuser_udwps_backtrace','/app/ns/udw/log/lighttpd_log_backtrace','/app/ns/udw/log/map_api_phpui_backtrace','/app/ns/udw/log/map_phpui_backtrace','/app/ns/udw/log/mobilemap_log_backtrace','/app/ns/udw/log/music_play_lighttpd_access_ecomon_backtrace','/app/ns/udw/log/nsclk_backtrace','/app/ns/udw/log/pcs-stor-lighttpd_backtrace','/app/ns/udw/log/searchbox_uac_android_udw_on_backtrace','/app/ns/udw/log/setup_udw_backtrace','/app/ns/udw/log/tc2_front_new/','/app/ns/udw/log/tc2_front_udw_on_new_backtrace','/app/ns/udw/log/ting_musicapp_acess_log_backtrace','/app/ns/udw/log/vs_as_xcloudboss_backtrace','/app/ns/udw/log/wapmaplighttpd_backtrace','/app/ns/udw/log/wapmap_backtrace','/app/ns/udw/log/wise-freeapp_backtrace','/app/ns/udw/log/wise_lighttpd2show_backtrace','/app/ns/udw/log/wise_phpui_search','/app/ns/udw/log/wise_phpui_show_udw_on','/app/ns/udw/log/wise_se_search_front_log','/log/30929/searchbox_uac_android_udw_on','/log/30929/tc2_front_udw_on','/log/30929/ub_searchbox_aiw_udw','/log/30929/wise_abnor_searchid_udw_on','/log/30929/wise_phpui_search_udw_on/','/log/30929/wise_phpui_show_udw_on/','/log/30929/wise_remora_show_udw_on']
'''
lbs_log_path=['/app/bigpipe/ECOM/SDC/tuanbai/ers_js/tuanbai-ers-js-log-pipe','/app/bigpipe/NS/map/mapbasic_log/ns-map-mapbasic-pipe','/app/bigpipe/NS/map/wapmap_log/ns-map-wapmap-pipe','/app/bigpipe/NS/map/webmap_log/ns-map-webmap-pipe','/app/bigpipe/VS/VSFL/ting/musicapp_acess_log/music-ting-musicapp-log-pipe','/app/bigpipe/NS/map/mobilemap_log/ns-map-mobilemap-pipe','log/30929/wise_phpui_show_udw_on/','/app/bigpipe/NS/map/mmproxy-client_log/ns-map-mmproxy-client-pipe','/app/bigpipe/NS/map/webmap-lighttpd_log/ns-map-webmap-lighttpd-pipe','/app/ns/udw/bigpipe/union-pipe/','/app/ns/udw/log/browser_criticaltech_udw_backtrace','/app/bigpipe/NS/map/wapmap_log/ns-map-wapmap-pipe','/app/bigpipe/ECOM/SDC/tuanbai/ers_js/tuanbai-ers-js-log-pipe','/app/ns/udw/bigpipe/union-pipe/','/log/34359/activeuser_udwps','/app/ns/udw/bigpipe/union-pipe']

ps_log_path = ['/app/bigpipe/MIC/sh_wise/bd_input_mmi_ci/sh-wise-db-input-mmi-ci-pipe','/app/bigpipe/MCO/CLOUD/HAO123/apache_access/mco-hao123-apache-pipe','/app/bigpipe/MIC/sh_wise/bd_input_mmi_ci/sh-wise-db-input-mmi-ci-pipe','/app/bigpipe/MCO/CLOUD/HAO123/apache_access/mco-hao123-apache-pipe','/log/34359/day_unsetup_udw','/log/34359/day_activeuser_udw','/app/bigpipe/NS/map/mobile-v1-iphone/mobile-v1-iphone-pipe']

wise_log_path = ['/app/bigpipe/PS/www/online/psclk/ps-clicklog-pipe','/log/30929/bws_abnor_udw_on','/app/ns/udw/log/ime_commitword_log_udw_backtrace']

def get_core_hour(queue_name, start_time, end_time):
    cmd      = MYSQL_STON + "select sum(cpu_used) from queue_cpu_usage where queue_name='" + queue_name + "' and log_time>='"+start_time + "' and log_time<'" + end_time + '\';"'
    to_print = "%s\n" % (cmd)
    print type(to_print)
    print to_print
    re  = os.popen(cmd).readlines()
    return re

def get_queue_name_by_username(user_name):
    cmd = "%s select distinct(queue_name) from job_info where user='%s';\"" % (MYSQL_DC,user_name)
    print cmd
    re  = os.popen(cmd).readlines()
    return re
    
def get_stattistic():
    cmd = MYSQL_DC + 'show tables;"'
    print cmd
    re  = os.popen(cmd).readlines()
    print re

def get_core_hour_by_username(user_name, start_time, end_time):
    queue_name      = get_queue_name_by_username(user_name)
    total_core_hour = 0
    for qn in queue_name[1:]:
        if (qn.strip()).find('idle') != 0:
            print qn
            tmp_count = ((get_core_hour(qn.strip(),start_time,end_time))[1]).strip()
            if tmp_count != 'NULL':
                total_core_hour = total_core_hour + int(tmp_count)
        else:
            print "idle queue is filt out"
    return total_core_hour

def get_slot_time(opt,start_time, end_time):
    if   opt==1:
        cmd = MYSQL_DC +"select sum(m.map_total_slot_time)+sum(m.reduce_total_slot_time) from job_info j,slot_time m where j.jobid=m.jobid and (j.jobname like '%lbs_map_its_control%' or j.jobname like '%lbs_wapmap%' or j.jobname like '%map_dingweiloc1%' or j.jobname like '%map_lighttpd_union%' or j.jobname like '%map_mmproxy%' or j.jobname like '%map_phpui%' or j.jobname like '%mapmobile%' or j.jobname like '%DN_lbc_inf%' or j.jobname like '%map_dingwei2%' or j.jobname like '%map_itscontrol2%' or j.jobname like '%map_mobile2%' or j.jobname like '%lbs_bigtable_full_outer_big%' or j.jobname like '%lbs_flocshare_mobile_join%') and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re  = os.popen(cmd).readlines()
        return re
    elif opt==2:
        cmd = MYSQL_DC + "select sum(m.map_total_slot_time)+sum(m.reduce_total_slot_time) from job_info j,slot_time m where j.jobid=m.jobid and (j.jobname like 'ps_click_union%' or j.jobname like 'ps_query_online%' or j.jobname like 'ps_view%' or j.jobname like 'ps_ud_detail%' or j.jobname like 'view_ps_ud_query_type_tmp1 %' or j.jobname like 'INSERT OVERWRITE TABLE view_ps_ %' or j.jobname like 'view_ps_ud_detail %' or j.jobname like 'view_ps_ud_se_pv_min_%' or j.jobname like 'insert overwrite%' ) and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re = os.popen(cmd).readlines()
        return re
        
    elif opt==3:
        cmd = MYSQL_DC + "select sum(m.map_total_slot_time)+sum(m.reduce_total_slot_time) from job_info j,slot_time m where j.jobid=m.jobid and (j.jobname like 'wise_ps_click_display_5%') and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re  = os.popen(cmd).readlines()
        return re
        
    else:
        print "Usage:\n opt=1--get lbs slot times\n opt=2--get ps slot time\n opt=3--get wise slot time" % ()

    
    
def get_map_input_bytes(opt,start_time, end_time):
    if   opt==1:
        cmd = MYSQL_DC +"select sum(m.map_input_bytes) from job_info j,map_counter m where j.jobid=m.jobid and (j.jobname like '%lbs_map_its_control%' or j.jobname like '%lbs_wapmap%' or j.jobname like '%map_dingweiloc1%' or j.jobname like '%map_lighttpd_union%' or j.jobname like '%map_mmproxy%' or j.jobname like '%map_phpui%' or j.jobname like '%mapmobile%' or j.jobname like '%DN_lbc_inf%' or j.jobname like '%map_dingwei2%' or j.jobname like '%map_itscontrol2%' or j.jobname like '%map_mobile2%' or j.jobname like '%lbs_bigtable_full_outer_big%' or j.jobname like '%lbs_flocshare_mobile_join%') and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re  = os.popen(cmd).readlines()
        return re
    elif opt==2:
        cmd = MYSQL_DC + "select sum(m.map_input_bytes) from job_info j,map_counter m where j.jobid=m.jobid and (j.jobname like 'ps_click_union%' or j.jobname like 'ps_query_online%' or j.jobname like 'ps_view%' or j.jobname like 'ps_ud_detail%' or j.jobname like 'view_ps_ud_query_type_tmp1 %' or j.jobname like 'INSERT OVERWRITE TABLE view_ps_ %' or j.jobname like 'view_ps_ud_detail %' or j.jobname like 'view_ps_ud_se_pv_min_%' or j.jobname like 'insert overwrite%' ) and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re = os.popen(cmd).readlines()
        return re
        
    elif opt==3:
        cmd = MYSQL_DC + "select sum(m.map_input_bytes) from job_info j,map_counter m where j.jobid=m.jobid and (j.jobname like 'wise_ps_click_display_5%') and j.finish_time>='" +start_time + "'"+ "and j.finish_time<'"+end_time + "'" + " and m.finish_time>='" +start_time + "'"+ "and m.finish_time<'"+end_time + "'"  +';"'
        print cmd
        re  = os.popen(cmd).readlines()
        return re
        
    else:
        print "Usage:\n opt=1--get lbs map_input_bytes\n opt=2--get ps map_input_bytes\n opt=3--get wise map_input_bytes" % ()

def get_cmd_result(opt, cmd):
    if (opt==0):
        cmd = cmd + '>/dev/null 2>&1; echo $?';
        re  = os.popen(cmd).readlines();
        re  = re[0].strip();
        return re;
    else:
        re  = os.popen(cmd).readlines();
        re  = re[0].strip();

        
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

def get_udw_log_size(opt,datetime):
    tmp_count         = 0
    if opt==1:
        tmp_count     = 0
        for path in lbs_log_path:
            path      = path + "/" + datetime
            tmp_count = tmp_count + float(get_per_path_size(HADOOP_CLIENT,path))
        tmp_count = float(tmp_count)/(1024*1024*1024)
        print datetime+" lbs_log_size:" + str(tmp_count)
        return tmp_count
    elif opt==2:
        tmp_count     = 0
        for path in ps_log_path:
            path      = path + "/" + datetime
            tmp_count = tmp_count + float(get_per_path_size(HADOOP_CLIENT,path))
        tmp_count = float(tmp_count)/(1024*1024*1024)
        print datetime+" ps_log_size:" + str(tmp_count)
        return tmp_count
    elif opt==3:
        tmp_count     = 0
        for path in wise_log_path:
            path      = path + "/" + datetime
            tmp_count = tmp_count + float(get_per_path_size(HADOOP_CLIENT,path))
        tmp_count = float(tmp_count)/(1024*1024*1024)
        print datetime+" wise_log_size:" + str(tmp_count)
        return tmp_count
    else:
        print "Usage:\n opt=1--get lbs log size\n opt=2--get ps log size\n opt=3--get wise log size" % ()

if __name__ == "__main__":
    #print    get_core_hour('ecomon-udw','2013-08-31','2013-09-01')
    #print get_queue_name_by_username('dt-udw-etl')
    #print get_queue_name_by_username('dt-udw-insight')

#    print  get_core_hour_by_username('dt-udw-insight','2013-08-31 00:00:00','2013-09-01 00:00:00')
#    print    "%f\n" % (float((get_map_input_bytes(3,'2013-08-30 00:00:00','2013-08-31 00:00:00'))[1].strip())/(1024*1024*1024*1024))
#    print get_slot_time(3,'2013-08-31 00:00:00','2013-09-01 00:00:00')
    print get_udw_log_size(2,'20130830')
