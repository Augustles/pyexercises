#-*-coding:utf-8-*-

import os

s = raw_input('��������Ҫ�����Ĵ��� :')
for i in os.walk(s):
    print i
	
for i in os.walk('s'):
    print i