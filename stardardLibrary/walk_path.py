
# coding=utf-8

import os
import os.path

# default log
'''
a = raw_input("please enter path:")
for root, dir, file in os.walk(a):
    for i in file:
        x = os.path.join(root, i)
        open(os.getcwd() + "/a.txt", "a+").writelines(x + "\n")
'''
print os.linesep + "lint:default write to ~/a.txt"


def walk_path():
    path = raw_input('请输入路径：')
    for i in os.listdir(path):
        x = os.path.join(path, i)
        if os.path.isfile(x):
            print x

if __name__ == '__main__':
    print 'start walk_path ...'
    walk_path()
