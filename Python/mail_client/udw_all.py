import common_lib
import os
import get_log_path
from common_lib import analysis_Dag,HADOOP_CLIENT,get_per_path_size
from get_log_path import get_log_path


MYSQL_DT_META_ONLINE = 'mysql -h10.46.104.60 -pMhxzKhl -P8357 -uroot offline -e "select distinct(name) from TblETLDagDef where dagStatus=1;" | awk \'{print $1}\''


def get_udw_dag_list():
    re           = os.popen(MYSQL_DT_META_ONLINE).readlines()
    tmp_dag_list = []
    for item in re[1:]:
        tmp_dag_list.append(item.strip())
    return tmp_dag_list
    
def get_udw_dag_log_dict():
    all_dags = get_udw_dag_list()
    udw_dag_log_dict = {}
    for item in all_dags[0:]:
        udw_dag_log_dict[item]  = analysis_Dag('1',item)
        for (k,v) in  udw_dag_log_dict.items():
            tmp_list            = []
            for va in v:
                tmp_list.append(va.strip())
            udw_dag_log_dict[k] = tmp_list
    return udw_dag_log_dict
    
def get_udw_dag_log_path_dict():
    udw_dag_log           = get_udw_dag_log_dict()
    udw_dag_log_path_dict = {}

    for (k,v) in udw_dag_log.items():
        path_list2    = []
        for va in v:
            path_list = get_log_path(va)
#            print "path_list len is " + str(len(path_list))
            path_list2.append(path_list[0].strip())
        udw_dag_log_path_dict[k] = path_list2
    return udw_dag_log_path_dict

def get_udw_log_size(datetime):
    dag_log_path          = get_udw_dag_log_path_dict()
    dag_log_size          = {}
    tmp_count             = 0
    for (dag,path_list) in dag_log_path.items():
        tmp_count         = 0
        for path in path_list:
            path          = path + "/" + datetime
            tmp_count     = tmp_count + float(get_per_path_size(HADOOP_CLIENT,path))
        dag_log_size[dag] = float(tmp_count)/(1024*1024*1024)
        print "dict[" + dag + "] = " + str(dag_log_size[dag])
    return dag_log_size

if __name__ == "__main__":
    ret = get_udw_log_size("20130827")
    for (k,v) in ret.items():
        print "dict[%s]" % k,v
