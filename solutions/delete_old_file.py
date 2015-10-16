# coding=utf-8

import os
import os.path
import time
import datetime
import shutil

# 也可以转化为struct_time比较


def delete_old_file(files):
    for file in files:
        stat = os.stat(file)  # 获取文件信息stat.st_ctime
        l_time = time.localtime(stat.st_ctime)  # 转化为struct_time
        l_time = datetime.datetime.fromtimestamp(
            time.mktime(l_time))  # 处理为datetime
        c_time = time.ctime(os.path.getctime(file))  # 获取文件创建时间str
        c_time = datetime.datetime.strptime(
            c_time, '%a %b %d %H:%M:%S %Y')  # 转化为datetime
        # c_time = time.strptime(c_time, '%a %b %d %H:%M:%S %Y') #
        # 转为stract_time
        if file.find('Report') == 0 and file.endswith('.xls'):
            now = datetime.datetime.now()
            bef_month = now + datetime.timedelta(days=-30)
            g_time = time.time() - 60 * 60 * 24 * 30  # 与stat.st_ctime比较
            gg_time = time.localtime(g_time)  # 转化为stract_time比较
            if bef_month > l_time:
                t_dir = r'c:\backup'
                if not os.path.exists(t_dir):
                    os.makedirs(t_dir)
                else:
                    shutil.copy(file, t_dir)
                    os.remove(file)

if __name__ == '__main__':
    base = r'C:\mongo\source'
    files = os.listdir(base)
    delete_old_file(files)
