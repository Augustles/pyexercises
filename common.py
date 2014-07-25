#-*-coding:utf-8-*-
import os
import time
import shutil
today = time.strftime('%Y-%m-%d星期%w')#today
now = time.strftime('%H:%M:%S') #打印now
print today
print now

'''os.path.sep ：#路径分隔符 。以前老爱用'\' ，windows返回'/'。
os.path.altsep：#（根目录，不是很确定，我用来做根目录。反正在windows表现是'/'）
os.path.curdir： #当前目录，
os.path.pardir： #父目录'''