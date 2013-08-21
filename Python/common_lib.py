import os
def get_cmd_result(opt, cmd):
    if (opt==0):
        cmd = cmd + '>/dev/null 2>&1; echo $?';
        re  = os.popen(cmd).readlines();
        re  = re[0].strip();
        return re;
    else:
        re  = os.popen(cmd).readlines();
        print re
        re  = re[0].strip();
        return re
if (__name__=='__main__'):
    re      = get_cmd_result(0,'xxx');
    print re;
