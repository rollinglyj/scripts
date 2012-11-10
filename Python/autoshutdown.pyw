#   @This script can be used to automaticly shutdown the operating system
#   @This script is running under python 3.1
#   @author:zhangchao
#   @email:uestchangchao@gmail.com
#   @Time:2011年7月27日20:03:51
###########################################################################
import os
choice=input("do you want to shutdown the system?y[yes] or n[no]\n")
if choice=="y" or choice=="Y" or choice=="YES" or choice=="yes":
    o="c:\\windows\\system32\\shutdown -s -t 120"
    os.system(o)
    print("system will shutdown in 120 Seconds,if you want to cancel run cmd line shutdown /a\n")

