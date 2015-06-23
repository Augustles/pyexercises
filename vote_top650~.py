# coding=utf-8

# stackoverflow vote top

# 导出pip freeze > requirements.txt
# 安装pip install -r requirements.txt
# 1.fill out a python string with spaces
f = 't'
print(f.zfill(3))
print(f.ljust(3),len(f.ljust(3)))
print(f.rjust(3))
# 2.what is the best way to implement nested dictionaries in python
# http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python
# 3.python:import a subdirectory
# http://stackoverflow.com/questions/1260792/python-import-a-file-from-a-subdirectory
# 4.python print string to textfile
# with open('test.txt', 'a+') as a, open('test1.txt', 'r+') as b:
#     pass
# file = open('test.txt', 'w+')
# file.write('hello world')
# 5.having django serve dowloadable files
# http://stackoverflow.com/questions/1156246/having-django-serve-downloadable-files
# 6.how to get current cpu and ram useage in python
import psutil
cpu_percent = psutil.cpu_percent();print(cpu_percent)
mem = psutil.virtual_memory();print(mem)
# 7.listing all function in python module
import os
vars(os)
dir(os)
# 8.how to get console window width in python
# http://stackoverflow.com/questions/566746/how-to-get-console-window-width-in-python
# 9.maxium and minmum values for ints
import sys
sys.maxint # 32位，2^32-1
sys.maxsize # python3
# 10.python access to first element in dictionary
d = { x:y for x,y in zip(range(2,5), range(3,7))}
x = d.itervalues().next()
# 11.how can i install $HOME folder
# pip install --user flask
