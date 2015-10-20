#!/usr/bin/env python
#-*- coding:utf-8 -*-


import time,os,sys

'''
定时关机, 添加linux
'''

def work():
    cmd = '''c:\\windows\\system32\\shutdown -s -f -t 60'''
    print u'''马上将要关机了，还有3分钟\r\n如果不想关机，输入shutdown -a'''.encode('gb2312','ignore')
    os.system(cmd)
    a = raw_input(u"输入n即可停止关机\r\n".encode('gb2312','ignore'))
    if a == 'n':
        cmd = '''c:\\windows\\system32\\shutdown -a'''
        os.system(cmd)
    time.sleep(60)
if __name__ == '__main__':
    num = int(time.strftime('%H'))
    if os.name == 'nt':
        if num >= 18:
            work()
    else:
        if num >= 18:
            print 'shutdown'
            os.system('halt')
