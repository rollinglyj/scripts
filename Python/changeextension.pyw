###########################################################################
#   @This script can be used to change file extension,the file is specified in a particular
# directory,the directory can be recursive.
#
#   @This script is running under python 3.1
#   @author:zhangchao
#   @Time:2010-10-14 
###########################################################################


import os
import string
import filecmp
   
def s_rename(path,old_ext,new_ext):
    print("old_ext:" + old_ext)
    for (path, dirs, files) in os.walk(path):    
        for filename in files:    
            ext=os.path.splitext(filename)[1]
            print("ext:" + ext)
              
            print("old_ext.rfind(ext):=" + str(new_ext.rfind(ext)))
            
            #if oldfilename not equql new filename
            #here when i use cmp(new_ext,ext),i got the wrong result!
            if (new_ext.rfind(ext) == -1):
                
                newname=filename.replace(old_ext,new_ext)
                print(newname)
                oldpath=path+"\\"+filename    
                newpath=path+"\\"+newname    
                print("oldpath"+oldpath+"")
                print("newpth:"+newpath+"")
                try:    
                    os.rename(oldpath, newpath)    
                except ValueError:    
                    print ("Error when rename the file " + oldpath)
                except NameError:    
                    print("Error when rename the file " + oldpath)
                except OSError:    
                    #print(OSError)
                    print(newpath + " The file is already exist!")
if __name__ == '__main__':    
    s_rename("F:\code",".txt",".php")    
    print("test")
