# encoding=utf-8

import md5
import os
from time import clock as now


def getmd5(filename):
    file_txt = open(filename, 'rb').read()
    m = md5.new(file_txt)
    return m.hexdigest()


def main(path):
    os.chdir(path)
    all_md5 = []
    total_file = 0
    total_delete = 0
    start = now()
    for file in os.listdir(path):
        total_file += 1
        file = os.path.abspath(file)
        if os.path.isfile(file) == True:
            filemd5 = getmd5(file)
            if filemd5 in all_md5:
                total_delete += 1
                print '删除', file
                os.remove(file)
            else:
                all_md5.append(filemd5)
    end = now()
    time_last = end - start
    print '文件总数：', total_file
    print '删除个数：', total_delete
    print '耗时：', time_last, '秒'

if __name__ == '__main__':
    path = os.getcwd()
    main(path)
