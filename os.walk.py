#-*-coding:utf-8-*-

import os

s = raw_input('请输入你要遍历的磁盘 :')
for i in os.walk(s):
    print i
	
for i in os.walk('s'):
    print i