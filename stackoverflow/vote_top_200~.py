# coding=utf-8

# stackoverflow top 151~200

# 151.correct way to write line to file in python   '\n'
# 152.how do i remove/delete a folder that is not empty with python
# shutil.rmtree()
# 153.how can i force division to be floating point in python
# from __future__ import division   其中一个为float
# 154.python create unix timestamp five minute in the future
from datetime import *
import calendar
future = datetime.utcnow() + timedelta(minutes = 5)
print future
print calendar.timegm(future.timetuple())
# 155.can someone explain __all__ in python
# link:http://stackoverflow.com/questions/44834/can-someone-explain-all-in-python
# 156.adding a method to an existing object
# link:http://stackoverflow.com/questions/972/adding-a-method-to-an-existing-object
# 157.count occurence of a character in a string
# str1.count('a') # 统计某个字符出现次数
# 158.how debug in django,the good way
# import ipdb ipdb.set_trace()
# 159.non-blocking read on a subprocess,pipe in python
# link:http://stackoverflow.com/questions/375427/non-blocking-read-on-a-subprocess-pipe-in-python
# 160.python -time.clock vs. time.time() accuracy
# link:http://stackoverflow.com/questions/85451/python-time-clock-vs-time-time-accuracy
# 161.null object in python   a is None:
# 162.installing specific package version with pip
# pip install django==1.5.8
# 163.how to remove a key from a dictionary
# d.pop(key, None) 返回key对应的value   del d[key]
# 164.is there a portable way to get the current username in python
import getpass
username = getpass.getuser()
# 165.checking whether a variable is an ingeger or not
# str1.isdigit()   .isalnum()
# 166.map two lists into a dictionary in python
# zip(key, value) from itertools import izip_longest izip_longest(key, value)
# 167.how can i print a literal '{}' characters in python string and also use .format on it
a = '{{ hello }} {0}'
print a.format(3)
# 168.how to find if directory exists in python
import os # os.path.isdir()
print(os.path.exists('vote_top_151_200.py'))
# 169.how to detect a christmas tree
# link:http://stackoverflow.com/questions/20772893/how-to-detect-a-christmas-tree
# 170.most elegant way to check if the string is empty in python
t = ''
if not t:print 1
# 171.do-while loop in python
# link:http://stackoverflow.com/questions/743164/do-while-loop-in-python
# 172.clang error:unkown argument:'-mno-fused-madd' python package installation failure
# link:http://stackoverflow.com/questions/22313407/clang-error-unknown-argument-mno-fused-madd-python-package-installation-fa
# 173.how to get the home directory in python
from os.path import expanduser
print(expanduser('~'))
# 174.is there any pythonic way to combine two dicts (adding value for keys that appear in both)
from collections import Counter
c = Counter({'a':1, 'b':2, 'c':3})
d = Counter({'b':3, 'c':4, 'd':5})
f = dict(c + d) # 
e = sorted(f.items(), key = lambda x:x[1]) # 根据value排序
print f,e
# 175.how do you change the size of figures drawn with matplotilb
# link:http://stackoverflow.com/questions/332289/how-do-you-change-the-size-of-figures-drawn-with-matplotlib
# 176.what are the differences between json and simplejson python modules
# use simplejson if possible
# 178.pylint, pychecker or pyfakes
# link:http://stackoverflow.com/questions/1428872/pylint-pychecker-or-pyflakes
# 179.how to install pscopg2 with 'pip' on python
# sudo apt-get install libpq-dev python-dev
# 180.getting the length of an array in python
print len(range(3,9))
# 181.python list comprehension vs. Map
# link:http://stackoverflow.com/questions/1247486/python-list-comprehension-vs-map
# 182UnicodeEncodeError:'ascii' codec can't encode charater u'\xa0' in position20 ordinaly not in range(128)
# link:http://stackoverflow.com/questions/9942594/unicodeencodeerror-ascii-codec-cant-encode-character-u-xa0-in-position-20 
# 183.how to do relative imports in python
# link:http://stackoverflow.com/questions/72852/how-to-do-relative-imports-in-python
# 184.writing unit tests in python: how i start
# link:http://stackoverflow.com/questions/3371255/writing-unit-tests-in-python-how-do-i-start
# 185.how do you retrun multiple values in python
# link:http://stackoverflow.com/questions/354883/how-do-you-return-multiple-values-in-python
# 186.creating constant in python
# link:http://stackoverflow.com/questions/2682745/creating-constant-in-python
# 187.what does the star operator mean in python   # 同前
# 188.how do i find the location of my python site-packages directory
import site
print(site.getsitepackages())
# 189.convert python dict to object
# link:http://stackoverflow.com/questions/1305532/convert-python-dict-to-object
d = {'a': 1, 'b': {'c': 2}, 'd': ["hi", {'foo': "bar"}]}
from collections import namedtuple
# 190.what soap client libraries exist for python, and where is the documentation for them
# link:http://stackoverflow.com/questions/206154/what-soap-client-libraries-exist-for-python-and-where-is-the-documentation-for
# 191.convert date to datetime in python
from datetime import *
d = date.today()
time = datetime.combine(d, datetime.min.time())
# 192.what is the difference between range and xrange functions in python2.x
# 193.how does python's super() work with multiple in heritance
# link:http://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
# 194.Try/Except in python: how do you properly ignore exceptions
try:
    10/0
except Exception, e:
    print e
# 195.paring values from a json file in python
# link:http://stackoverflow.com/questions/2835559/parsing-values-from-a-json-file-in-python
# 196.comprehensive beginner's virtualenv tutorial
# 197.why are python's 'private' methods not actuall private
# link:http://stackoverflow.com/questions/70528/why-are-pythons-private-methods-not-actually-private
# 198.how to check file size inpython
import os
statinfo = os.stat('vote_top_151_200.py')
print statinfo.st_size,statinfo
# 199. how to install lxml on ubuntu
# apt-get install libxml2-dev libxslt1-dev python-dev
# 200.'large data' work flows using pandas
# link:http://stackoverflow.com/questions/14262433/large-data-work-flows-using-pandas
