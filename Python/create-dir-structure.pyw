#   @This script can be used to iterate the given directory,and create the 
#   empty directory structure without file in it,e.g,I want to have you directory
#   as the linux kernel source, but i don't want the files, then this script comes.
#   @This script is running under python 3.1
#   @author:zhangchao
#   @Time:2011年7月25日18:43:26
###########################################################################


import os
import re

#listmydirs is created to recursivly list all the entrys in the specified path.
#In fact, we have os.walk to handle this problem

#
#level:目录的层数，不要也可以，主要是为了显示目录在那一层
#srcpath:内核源代码所在的路路径
#destpath:将要生成的内核源代码的目录结构所在路径
#

def createkerneldirs(level,srcpath,destpath):
    for entrys in os.listdir(srcpath): #学习listdir函数的用法
        tmpsrcpath=srcpath+os.sep+entrys
        tmpdestpath = tmpsrcpath.replace(srcpath,destpath)#将源路径中的E:\linux-2.6替换为E:\tmp,学习字符串替换函数的用法
  
        print('in level:'+str(level))
        print(tmpsrcpath)
        print(tmpdestpath)
        
        if os.path.isdir(tmpsrcpath):
            listmydirs(level+1,tmpsrcpath,tmpdestpath)
            if os.path.exists(tmpdestpath)==False: #如果文件不存在才创建文件
                os.makedirs(tmpdestpath)

if __name__=='__main__':
#将E:\linux-2.6的内核源代码目录结构拷贝到E:\tmp目录下
    createkerneldirs(1,r'E:\linux-2.6',r'E:\tmp')

