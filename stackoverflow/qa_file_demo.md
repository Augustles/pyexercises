
1 如何判断一个文件是否存在
import os.path
print os.path.isfile('qa_file.py')
print os.path.exists('qa_file.py')
2 如何创建不存在的目录
if not os.path.exists('tmp'):
    os.makedirs('tmp')
3 如何拷贝一个文件
import shutil
shutil.copyfile('qa_file.py','qa_file_demo.py')
4 逐行读文件去除换行符(perl chomp line)
text = "line 1\nline 2\r\nline 3\nline 4"
text.splitlines();print text
5 如何获取一个文件的创建时间和修改2015年5月19日时间
import os.path, time
print 'last modified: %s' %time.ctime(os.path.getmtime('qa_file.py'))
print 'created: %s' %time.ctime(os.path.getctime('qa_file.py'))
6 如何将字符串转化为datetime
from datetime import datetime
demo = datetime.strptime('Mon Mar 09 18:35:20 2015', '%a %b %d %H:%M:%S %Y')
date_object = datetime.strptime('Jun 1 2015  1:33PM', '%b %d %Y %I:%M%p')
print date_object
7 如何找到一个目录下所有.txt文件
import os
os.chdir('tmp') # 改成需查找的目录
for files in os.listdir('tmp'):
    if files.endswith('.txt'):
        print files

for r,d,f in os.walk('tmp'):
    for files in f:
        if files.endswith('.txt'):
            print os.path.join(r,files)

8 读文件到列表中
with open('qa_file.py') as fp:
    content = fp.readlines()
9 如何往文件中追加文本
with open('qa_file_demo.py','a') as fp:
    fp.write('append line')
10 如何获取文件扩展名
path = os.chdir(r'C://users/ieware')
print path
filename, extension = os.path.splitext('.')
print filename
append line