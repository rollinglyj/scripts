import os
import sys
MYSQL_DC='mysql -h10.220.156.34 -udc_user -pdc_user -P3306 -D SZWG_ECOMON -e "'
MYSQL_STON = 'mysql -h10.220.156.34 -udc_user -pdc_user -P3306 -D SZWG_STON -e "'

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

        

if __name__ == "__main__":
    #print    get_core_hour('ecomon-udw','2013-08-31','2013-09-01')
    #print get_queue_name_by_username('dt-udw-etl')
    #print get_queue_name_by_username('dt-udw-insight')

#    print  get_core_hour_by_username('dt-udw-insight','2013-08-31 00:00:00','2013-09-01 00:00:00')
#    print    get_map_input_bytes(3,'2013-08-31 00:00:00','2013-09-01 00:00:00')
    print get_slot_time(3,'2013-08-31 00:00:00','2013-09-01 00:00:00')
