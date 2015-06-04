# coding=utf-8

import os,os.path
import time
import datetime
import shutil

base = r'C:\mongo\source'
files = os.listdir(base)
for file in files:
    stat = os.stat(file)
    l_time = time.localtime(stat.st_ctime)
    l_time = datetime.datetime.fromtimestamp(time.mktime(l_time))
    c_time = time.ctime(os.path.getctime(file))
    if file.find('Report') == 0:
        now = datetime.datetime.now()
        bef_month = now + datetime.timedelta(days=-30)
        if bef_month > l_time:
            shutil.copy(file,r'c:\backup')
            os.remove(file)
