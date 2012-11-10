#   @This script is used to recursively copy os application directories.   
#   @This script is running under python 3.1
#   @author:zhangchao
#   @email:uestczhangchao@gmail.com
#   @Time:2011年7月25日18:50:40
###########################################################################

import distutils.dir_util
import os
test_srcdir=r"X:\\实验室工作\\源代码\\调度表+时间保护\\ALL_TEST"
test_destdir=r"E:\autosar项目\source_code\\ALL_TEST"
distutils.dir_util.copy_tree(test_srcdir,test_destdir)

os_srcdir=r"X:\\实验室工作\\源代码\\调度表+时间保护\\os"
os_destdir=r"E:\autosar项目\source_code\os"

distutils.dir_util.copy_tree(os_srcdir,os_destdir)

cmd=r"X:\\编程练习\\脚本代码\\Python\\messagebox.exe"
os.system(cmd)






