#   @This script is used to recursively copy directories.   
#   @This script is running under python 3.1
#   @author:zhangchao
#   @Time:2011年7月25日18:50:40
###########################################################################

import distutils.dir_util
#The next line will recursively copy all the contents in E:\\TC to E:\\tmp
distutils.dir_util.copy_tree('E:\\TC','E:\\tmp')
