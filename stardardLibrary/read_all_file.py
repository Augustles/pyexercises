import os,os.path
import ipdb # pip install ipdb 彩色pdb

# 读取所有文件到tst.txt中
base_dir = r'c:/users/ieware'
for x in os.listdir(base_dir):
    if os.path.isfile(x):
        ipdb.set_trace()
        path = base_dir + "/" + x + '\n'
        with open('tst.txt','a') as f:
            f.write(path)
