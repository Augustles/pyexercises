# coding=utf-8
import os,datetime


try:
    base_dir = r'd:\ttoo'
except OSError, e:
    print '没有这个文件',e
list = os.listdir(base_dir)  # 得到一个包含文件和文件夹的列表
filelist = []
for i in range(0, len(list)):
    path = os.path.join(base_dir, list[i]) # 返回一个完整路径
    if os.path.isfile(path) == 1: # 判断是否为文件
        mtime = os.path.getmtime(path) # 文件的修改时间
        print mtime
        date = datetime.datetime.fromtimestamp(mtime)
        print list[i],' file最近修改时间是: ',date.strftime('%Y-%m-%d %H:%M:%S')
    else:
        mtime = os.path.getmtime(path)
        print mtime
        date = datetime.datetime.fromtimestamp(mtime)
        print list[i],' dir最近修改时间是: ',date.strftime('%Y-%m-%d %H:%M:%S')

