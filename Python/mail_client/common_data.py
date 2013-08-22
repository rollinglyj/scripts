
dag_list                 = ["nova_ad_display","columbus_ad_display","ps_query_online","wise_ps_click_display_5","udwetl_baidustat4uap","udwetl_houyi4uap","ps_click_union","dag_baike","dag_hao123click","sobar","udwetl_fc_dorado","udwetl_bdclk4uap","udwetl_holmes4uap"]

HADOOP_CLIENT = "~/Tool/hadoop-ecomon/bin/hadoop"
MYSQL_QA = 'mysql -h10.216.121.31 -uroot -pMhxzKhl -D udwbenchmark -e "'


dict_slot_time           = {}
dict_map_input_bytes     = {}
yes_dict_slot_time       = {}
yes_dict_map_input_bytes = {}
delta_slot_time           = {}
delta_map_input_bytes = {}




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
                "udwetl_baidustat4uap":['/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event/event_action=baidustat4uap_event'],
                "dag_baike":['/app/ns/udw/release/warehouse/udwetl_baikedummy/event_action=baikedummy','/app/ns/udw/release/warehouse/udw_event/event_action=baikeview','/app/ns/udw/release/warehouse/udw_event/event_action=baikeedit','/app/ns/udw/release/warehouse/udw_event/event_action=baikesearch','/app/ns/udw/release/warehouse/udw_event/event_action=baikeother'],
                "udwetl_bdclk4uap":['/app/ns/udw/release/warehouse/udwetl_bdclk4uap_event/event_action=bdclk4uap_event'],
                "columbus_ad_display":['/app/ns/udw/release/warehouse/udw_event/event_action=clbaddisplay'],
                "udwetl_fc_dorado":['/app/ns/udw/release/warehouse/udwetl_fcadclick_2/event_action=fcadclick_2'],
                "dag_hao123click":['/app/ns/udw/release/warehouse/udw_event/event_action=hao123webclk',],
                "udwetl_houyi4uap":['/app/ns/udw/release/warehouse/udwetl_houyi4uap_event/event_action=houyi4uap_event'],
                "udwetl_holmes4uap":['/app/ns/udw/release/warehouse/udwetl_holmes4uap_event/event_action=holmes4uap_event'],
                "nova_ad_display":['/app/ns/udw/release/warehouse/udw_event/event_action=novaaddisplay',],
                "ps_click_union":['/app/ns/udw/release/warehouse/udwetl_ps_clickdata/event_action=ps_clickdata','/app/ns/udw/release/warehouse/udw_event/event_action=ps_click'],
                "ps_query_online":['/app/ns/udw/release/warehouse/udwetl_other_webview/event_action=other_webview','/app/ns/udw/release/warehouse/udw_event/event_action=ps_query','/app/ns/udw/release/warehouse/udw_event/event_action=ps_index'],
                "wise_ps_click_display_5":['/app/ns/udw/release/warehouse/udwetl_wisepsclick_2/event_action=wisepsclick_2','/app/ns/udw/release/warehouse/udwetl_wisepsdisplay_2/event_action=wisepsdisplay_2','/app/ns/udw/release/warehouse/udwetl_wisepsunion_anti_2/event_action=wise_session_split'],
                "sobar":['/app/ns/udw/release/warehouse/udwetl_sobarurldata/event_action=sobarurldata']
}

input_size_dict        = {}
output_size_dict       = {}
yes_input_size_dict    = {}
yes_output_size_dict   = {}
delta_input_size_dict  = {}
delta_output_dize_dict = {}



'''
dag_list        = ["dag_baike","udwetl_baidustat4uap",]
dag_input_dict  = {"udwetl_baidustat4uap":['/log/11523/baidustat_holmes_session_et2'],"dag_baike":['/log/100025586/baike_nginx_access_2ecomon']}
dag_output_dict = {
                   "udwetl_baidustat4uap":['/app/ns/udw/release/warehouse/udwetl_baidustat4uap_event/event_action=baidustat4uap_event'],
                   "dag_baike":['/app/ns/udw/release/warehouse/udwetl_baikedummy/event_action=baikedummy','/app/ns/udw/release/warehouse/udw_event/event_action=baikeview','/app/ns/udw/release/warehouse/udw_event/event_action=baikeedit','/app/ns/udw/release/warehouse/udw_event/event_action=baikesearch','/app/ns/udw/release/warehouse/udw_event/event_action=baikeother'],}

'''
