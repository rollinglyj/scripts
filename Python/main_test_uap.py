import uap_statistic
import os
import common_lib
from uap_statistic import get_input_report, get_output_report

if __name__=='__main__':
    #uap_statistic.get_input_report('20130818','20130819')
    cmd = 'cat xxx >/dev/null 2>&1 ; echo $?'
    cmd = uap_statistic.HADOOP_CLIENT + ' fs -ls  /...app > /dev/null 2>&1; echo $?'
    print common_lib.get_cmd_result(1,cmd)

    
    
    
