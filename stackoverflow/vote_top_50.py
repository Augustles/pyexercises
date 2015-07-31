# coding=utf-8

# python vote top

# 1.what does the yield keyword do in python
# 返回一个可迭代的对象
# 2.what is a metaclass in python
# 类是元类的实例, 有类才有实例
# 3.cheak whethe a file exists using python
import os.path
os.path.isfile('vote_top_50.py')
# 4.does python have a ternary conditional operator 三元运算符
2 if 1 else 3
# 5.how can i make a chain of function decorators in python 装饰器
# 6.calling an external command in python
import os
os.system('ls') # os.system('ls > out.txt| vi test.txt < out.txt')
import subprocess
t = subprocess.check_output('ipconfig') # 返回回显内容
# http://stackoverflow.com/questions/89228/calling-an-external-command-in-python
# 7.how can i represent an 'enum' in python
# 8.how to install pip on windows # 设置path /scripts
# 9.how can i merge two python dictionaries in single expression
x = dict({'a':1,'b':2}.items() + {'c':3}.items()) # d.update(d1)
# 10.sort a python dictionary by value
r = sorted(x.items(), key=lambda x:x[1])
import operator
s = sorted(x.items(), key=operator.itemgetter(1))
# 11.what does 'if __name__ =  "__main__": ' do
# 判断是否直接运行还是import
# 12.using global variables in a function other than the one that created them   global
# 13.what ide to use for python vim sublime pycharm
# 14.is there a way to run python on android
# 15.in python check if a directory exists and create it if necessary
if not os.path.exists('testdir'):
    os.makedirs('testdir')
# 16.what is th difference between @staticmethod and @classmethod in python
# 隐含参数
# 17.'least astonishment' in python: the mutable default argument 变化的变量
# 18.best way to check if a list is empty   not list
# 19.how do i pass a variable by refernce
# 20.understanding  python super() with __init__() method
# 21.python append vs. extend extend方法把把每个子元素添加进去
# 22.difference between __str__ and __repr__ in python
# __str__ for human, __repr__ for program
# 23.accessing the index python for loops
for index,value in enumerate(range(5,9)):
    print index+1,value
# 24.does python have a string contains method
if 'ast' in 'astonishment':
    print 1
# 25.add key to a dictionary in python
x['tom'] = 23
# 26.explain python's slice notation   切片
# 27.how to list all files of a directory in python os.listdir()
os.chdir('.') # 改变工作目录
os.listdir('.') # 列出文件
# 28.how can i remove (chomp) a newline in python
y = '\t in astonishment \n'
y.strip() # 去除左右空格,rstrip,lstrip
t = y.replace(' ','.') # 注意replace改变的不是y的值
# 29.print terminator with colors using python   pip install termcolor
# 30.static class varables in python
class Myclass:
    i = 3
c = Myclass()
c.i = 4
print Myclass.i,c.i
# 31.static methods in python
# 32.parse string to float or int   int(), float()
a = '234.2'
int(float(a)) # 直接int报valueerror
# 33.how to get current time in python
import datetime
now = datetime.datetime.now();print now
now_format = now.strftime('%Y-%m-%d %H:%M:%S');print now_format
from time import gmtime, strftime
strftime("%Y-%m-%d %H:%M:%S", gmtime())
# 34.how to get the size of a list   len()
# 35.why is reading lines from stdin much slower in c++ than python
# 36.finding the index of an item given a list containing it in python
zz = ['tom', 'jim', 'lucy'].index('lucy') # 判读一个list是否有某个值
# 37.python join, why is string.join(list) instead of list.join(string)
lst = ["Hello", "world"]
'-'.join(lst)
# 38.why use pip over easy_install   pip
# 39.how do you read from stdin in python input???
# 40.how do i check a string is a number (float) in python
b = "963b";print b.isdigit()
# 41.how do you split a list into evenly sized chunks in python
import pprint
def chunks(l, n):
    for x in xrange(0, len(l), n):
        yield l[x:x+n]
pprint.pprint(list(chunks(range(10, 75), 10)))
# 42.is there a way to substring a string in python 子串:采用切片
# 43.check if a given key already exists in dictionary
if 'tom' in x:print 1
# 44.making a flat list out of lists in python [duplicate]
# 45.peak detection in a 2d array
lst1 = [[1,2,3],[4,5,6], [7], [8,9]]
lst2 = [y for x in lst1 for y in x]
# 46.how do i ramdomly select an item from a list using python
import random
foo = ['a', 'b', 'c', 'd', 'e']
ran = random.choice(foo);print ran # random.
# 47.how do sort a list of dictionaries by values of the dictionary in python   同10
# 48.how do i copy a file in python
import shutil
shutil.copy('vote_top_50.py', 'test.txt')
# 49.why does python code run faster in a function
