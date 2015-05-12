# coding=utf-8

import os
# 合并文件夹的内容
def mergeFiles(base_dir,out_file='demo.txt'):
    list_dir = os.listdir(base_dir)
    filelist = []
    for x in range(len(list_dir)):
        path = os.path.join(base_dir,list_dir[x])
        with open(path) as fp:
            with open(out_file,'a') as f: # 添加到文件
                for line in fp:
                    s = ''
                    line += s
                    f.writelines(line) # 写入到文件里

if __name__ == '__main__':
    base_dir =  r'D:\test\translation'
    #t = r'D:\test\translation\test.txt'
    mergeFiles(base_dir)
