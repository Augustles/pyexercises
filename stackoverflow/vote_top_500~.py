# coding=utf-8

# stackoverflow vote top
# 批量注释,批量解开注释

# 1.how to check django version
# import django
# print django.VERSION
# 2.what is the purpose of the single underscore '_' variable in python
# link:http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
# 3.how do i sort a list of strings in python
# 4.getting the sql from a django queryset
# link:http://stackoverflow.com/questions/3748295/getting-the-sql-from-a-django-queryset
# 5.are there any analysis tools for python
# pylint pychecker pyflakes
# 6.how to check whether two lists are circularly indentical in python
# link:http://stackoverflow.com/questions/26924836/how-to-check-whether-two-lists-are-circularly-identical-in-python
# 7.why does (1 in [1,0] == True) evaluate to False
# 8.how to install python3 version of package via pip on ubuntu
# link:http://stackoverflow.com/questions/10763440/how-to-install-python3-version-of-package-via-pip-on-ubuntu
# 9.test if executeable exists in python
# link:http://stackoverflow.com/questions/377017/test-if-executable-exists-in-python
# 10.syntax error on print with python 3
# python3 print is a function
# 11.plot logarithmic axes with matplotlib in python
# link:http://stackoverflow.com/questions/773814/plot-logarithmic-axes-with-matplotlib-in-python
# 12.python thread pool similar to the multiprocessing pool
# link:http://stackoverflow.com/questions/3033952/python-thread-pool-similar-to-the-multiprocessing-pool
# 13.using django time/date widgets in custom form
# link:http://stackoverflow.com/questions/38601/using-django-time-date-widgets-in-custom-form
# 14.get exception description and stack trace which caused an exception,all as a string
# link:http://stackoverflow.com/questions/4564559/get-exception-description-and-stack-trace-which-caused-an-exception-all-as-a-st
# 15.unicode (utf8) reading and writing to files in python
# link:http://stackoverflow.com/questions/491921/unicode-utf8-reading-and-writing-to-files-in-python
# 16.how to comment out a block of python code in vim
# ctrl+v block visual mode,选择要注释行,大写I插入,#或者//,如何esc
# link:http://stackoverflow.com/questions/2561418/how-to-comment-out-a-block-of-python-code-in-vim
# 17.how do i keep python print from  adding newlines or spaces
import sys
sys.stdout.write('hello world')
# 18.initialise a list to a specfic length in python
# link:http://stackoverflow.com/questions/983699/initialise-a-list-to-a-specific-length-in-python
# 19.how to use xpath in python
# link:http://stackoverflow.com/questions/8692/how-to-use-xpath-in-python
# 20.join list of lists in python
x = [["a","b"], ["c"]]
import itertools
print(list(itertools.chain(*x)))
# 21.what's the difference between a python module and a python package
# module is a file, package is usually a dir
# 22.find all packages installed with easy_install/pip
# pip list or pip freeze
# 23.python dictionary from an object's fields
# link:http://stackoverflow.com/questions/61517/python-dictionary-from-an-objects-fields
# 24.working with utf-8 encoding in python code
# coding=utf-8
# link:http://stackoverflow.com/questions/6289474/working-with-utf-8-encoding-in-python-source
# 25.python, path of script
import os
print(os.__file__)
# 26.is it possible to run a python script as a service in windows if possible,how
# link:http://stackoverflow.com/questions/32404/is-it-possible-to-run-a-python-script-as-a-service-in-windows-if-possible-how
# 27.strip html from strings in python
# link:http://stackoverflow.com/questions/753052/strip-html-from-strings-in-python
# 28.how do i design a class in python
# link:http://stackoverflow.com/questions/4203163/how-do-i-design-a-class-in-python
# 29.determine if variable is defined in python
try:
    ttt
except Exception, e:
    print e
else:
    print('sure, it was defined')
# 30.putting a simple if-then statement on one line
'yes' if x == 1 else 'no'
# 31.get difference between two lists
t1 = ['One', 'Two', 'Three', 'Four']
t2 = ['One', 'Two']
t3 = list(set(t1) - set(t2));print t3
# 32.what can you use python generator function for
# link:http://stackoverflow.com/questions/102535/what-can-you-use-python-generator-functions-for
# 33.how to use 'super' in python
# link:http://stackoverflow.com/questions/222877/how-to-use-super-in-python
# 34.python:about catching any exception
# try:
#     pass
# except Exception, e:
#     print e
# 35.split a string by spaces -- preserving quoted substrings -- in python
# 36.importing files from different folder in python
ttt = 'this is "a test"'
import shlex
import re
print(re.split(' ', ttt))
print(shlex.split(ttt))
print(ttt.split())
# link:http://stackoverflow.com/questions/4383571/importing-files-from-different-folder-in-python
# 37.find which version of package is installed with pip
# pip show django brew info git
# 38.why compile python code
# python -O -m test.py   .pyo是优化编译后的程序
# .pyc is much faster than .py
# 39.pip install lxml error
# sudo apt-get install libxml2-dev
# sudo apt-get install libxslt1-dev
# sudo apt-get install python-dev
# 40.getting file size in python
import os
print(os.path.getsize('vote_top_500~.py'))
print(os.stat('vote_top_500~.py').st_size)
# 41.reloading submodules in ipython
# link:http://stackoverflow.com/questions/5364050/reloading-submodules-in-ipython
# 42.what does python file extensions,.pyc,.pyd,.pyo stand for
# .pyc is compiled bytecode .pyo is optimization, .pyd is basically a windows dll
# 43.the difference between exit() and sys.exit() in python
# exit() is use in shell, sys.exit() use in program
# 44.understanding dict.copy() - shallow or deep
# link:http://stackoverflow.com/questions/3975376/understanding-dict-copy-shallow-or-deep
# 45.pythonic way to create a long multi-line string
s = ''' this is a very
        long string if i had the
        energy to tpye more and more...'''
# 46.relationship between scipy and numpy
# link:http://stackoverflow.com/questions/6200910/relationship-between-scipy-and-numpy
# 47.installing setuptools on 64-bit windows
# link:http://stackoverflow.com/questions/3652625/installing-setuptools-on-64-bit-windows
# 48.search and replace a line in a file in python
# link:http://stackoverflow.com/questions/39086/search-and-replace-a-line-in-a-file-in-python
# 49.python pip install fails:invalid command egg_info
# pip install --upgrade setuptools or easy_install -U setuptools
# 50.how to manager local vs. production settings in django
# link:http://stackoverflow.com/questions/1626326/how-to-manage-local-vs-production-settings-in-django
