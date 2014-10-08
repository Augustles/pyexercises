
#-*-coding:utf-8-*-

import os,os.path

#default log
a = raw_input("please enter path:")
for root,dir,file in os.walk(a):
    for i in file:
    	x = os.path.join(root,i)
        open(os.getcwd() + "/a.txt","a+").writelines(x + "\n")

print os.linesep + "lint:default write to ~/a.txt"