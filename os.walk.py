#-*-coding:utf-8-*-

import os
def walk_path():
    path = raw_input('请输入路径：')
    for i in os.listdir(path):
        x = os.path.join(path,i)
        if os.path.isfile(x):
            print x

	
if __name__ == '__main__':
    walk_path()
    print 'start walk_path'
