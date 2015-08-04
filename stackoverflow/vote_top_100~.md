
stackoverflow 51~100

51. error:unable to find vcvarsall.bat
52. why is `1000000000000000 in range(1000000000000001)` so fast?
53. python string formatting: % vs. .format # 尽量使用.format
54. how can you profile a python sript
55.*args and **kwargs?[duplicate] () {}
56. replacements for switch statement in python   use dict
def f(x):
    return {
        'a': 1,
        'b': 2,
    }.get(x, 9) # 没找到返回9
print f('b')
57. calling a function of a module from a string with the function's name in python
58. getting the class name of an instance in python   __name__
59. how can make a time delay in python
import time
time.sleep(0.5) # delays for 0.5 seconds
60. python:read file line by line into array
with open('vote_top_51_100.py') as f:
    content = f.readlines()
61. how to know if an object has an attribute in python
a = 'hello word'
if hasattr(a, '__len__'):
    print a.__len__
62. getting the last element of a list in python   [-1]
63. reverse a string in python
print a[::-1]
print '_'.join(a.strip().split()[::-1])
64. python:create a dictionary with list comprehension
x = {i:j for (i,j) in zip(range(1,9), range(3,12))};print x
65. merge two lists in python
listone = [1,2,3]
listtwo = [4,5,6]
merge = listone + listtwo # l.extend(list)
66. upgrading all packages with pip
pip freeze --local | grep -v '^\-e' | cut -d = -f 1  | xargs -n1 pip install -U
67. determine the type of an object
print type(listone),isinstance(listtwo,list)
68. converting string into datetime
from datetime import datetime
str_time = 'Jun 1 2005  1:33PM'
date_object = datetime.strptime(str_time, '%b %d %Y %I:%M%p');print date_object
69. how do i remove packages installed with python's easy_install
easy_install -m [PACKAGE]
rm -rf .../python2.X/site-packages/[PACKAGE].egg
70. what does ** (double star) and * do for python parameters
71. manually raising (throwing) an exception in python
raise Exception("I know python!")
72. random string generation with upper case letters and digits in python
import random
import string
str1 = ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(8))
more security version
str2 = ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.ascii_lowercase + string.digits) for _ in range(9))
print str1,str2
73. import a module from a relative path
import sys
sys.path.append(path)
import module
74. iterating over dictionaries using loops in python
dict.items(),d.keys(),d.values(),d.iteritems(),d.iterkeys(),d.itervlalues()
75. how to convert string to lowercase in python
string.lower(),string.upper()
76. how to print to stderr in python
77. how do i connect to a mysql databse in python
pip install mysql-python
78. the meaning of a single and a double-underscore before an object name
79. how to clone or copy a list in python
import copy
lst1 = listone[:];lst1 = list(listone)
lst1 = copy.copy(listone);lst1 = copy.deepcopy(listone)
80. how to leave/exit/deactivate a python virtualenv 
which virtualenvwrapper deactivate/workon test
pip install virtualenv && pip install virtualenvwrapper
81. what is __init__.py for
it is a part of packages
82. how to trim whitespace (include tabs)
string.strip(),string.rstrip(),string.lstrip()
83. how to print in python without newline or space
print('hello',end='') # print??
84. in python, how do i determine if an object is iterable
hasattr(obj, '__iter__') (o for o in obj)
85. nicest way to pad zeroes to string
n = '3'
print n.zfill(8)
86. find all files in directory with extendsion .txt with python
import os
base_dir = os.chdir('.')
filename = os.listdir('.')
for file in filename:
    if file.endswith('.txt'):
        print file
87. how to flush output of python print
import sys
sys.stdout.flush()
88. what's the canonical way to check for type in python   典型方法
95. extracting extension from filename in python
test_str = r'C:\Users\ieware\ttoo.py'
filename, fileExtension = os.path.splitext(test_str)
print filename,fileExtension
89. how do you append to a file in python
with open('test.txt') with fp:
    fp.write('append')
90. what is the difference between old style and new style class in python
91. find current directory and file's directory   os.getcwd()
os.path.dirname(os.path.realpath(__file__))
92. trmming a string in python   string.strip()
93. what is a mixin, and why are they useful
94. which python memory profiler is recommend [closed]
95. differences between distribute,distutils,setuptools and distutils2
96. differences between isinstance() and type() in python
97. python @classmethod and @staticmethod for beginner
98. what is th purpose of self in python   
绑定实例的属性
99. proper way to declare custom exceptions in moderm python
定制自己的exception
def myException(Exception):
    pass
