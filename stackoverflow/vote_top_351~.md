
stackoverflow top 351~

1. renaming columns in pandas
link:http://stackoverflow.com/questions/11346283/renaming-columns-in-pandas
2. running shell command from python and capturing the output
import subprocess
out = subprocess.check_output('ipconfig')
3. is there any difference between 'foo is None' and 'foo == None'
link:http://stackoverflow.com/questions/26595/is-there-any-difference-between-foo-is-none-and-foo-none
4. how do i find the location of python module sources
print subprocess.__file__
5. how do i run python code from sublime text 2
6. how can i open multiple files using 'with open' in python
with open('test.txt') as a, open('b') as b:
    pass
7. what do *args and **kwargs mean
8. how do i determine if my python shell is executing in 32bit or 64bit mode on os x
link:http://stackoverflow.com/questions/1405913/how-do-i-determine-if-my-python-shell-is-executing-in-32bit-or-64bit-mode-on-os
9. why doesn't python have multiline comments
10. how do i convert datetime to date in python
import datetime
now = datetime.datetime.now() # datetime.datetime object
now = now.date() # convert to datetime.date object
11. elegant python function to convert camelcase to camel_case
link:http://stackoverflow.com/questions/1175208/elegant-python-function-to-convert-camelcase-to-camel-case
import re
def convert(name):
    s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
    return re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
print convert('camelcase')
12. python:how to make a class json serializable
link:http://stackoverflow.com/questions/3768895/python-how-to-make-a-class-json-serializable
13. what are class methods in python for
link:http://stackoverflow.com/questions/38238/what-are-class-methods-in-python-for
14. typical augular.js workflow and project structure (with flask)
link:http://stackoverflow.com/questions/11522151/typical-angular-js-workflow-and-project-structure-with-python-flask
15. converting from a string to boolean in python
link:http://stackoverflow.com/questions/11522151/typical-angular-js-workflow-and-project-structure-with-python-flask
16. how to sort a list of objects in python, based on an attrbute of the objects
link:http://stackoverflow.com/questions/403421/how-to-sort-a-list-of-objects-in-python-based-on-an-attribute-of-the-objects
17. how do i use python's itertools.groupby()
link:http://stackoverflow.com/questions/773/how-do-i-use-pythons-itertools-groupby
18. running unitest with typical test directory structure
link:http://stackoverflow.com/questions/1896918/running-unittest-with-typical-test-directory-structure
19. is there a simple way to delete a list element by value in python
lst1 = range(9,2,-1)
lst1.remove(3);print lst1
20. how to re import an updated package while in python interpreter
link:http://stackoverflow.com/questions/684171/how-to-re-import-an-updated-package-while-in-python-interpreter
21. chain-calling parent constructors in python
link:http://stackoverflow.com/questions/904036/chain-calling-parent-constructors-in-python
22. python: what os am i running on
import os
os.name
23. flatten (an irregular) list of lists in python
link:http://stackoverflow.com/questions/2158395/flatten-an-irregular-list-of-lists-in-python
l = [[[1, 2, 3], [4, 5]], 6]
l1 = [y for x in l for y in x];print l1
24. how to save a python interactive session   ipython
link:http://stackoverflow.com/questions/606516/python-graph-library
25. creating a json response using django and python
link:http://stackoverflow.com/questions/2428092/creating-a-json-response-using-django-and-python
26. why is 'except: pass' a bad programming practice
link:http://stackoverflow.com/questions/21553327/why-is-except-pass-a-bad-programming-practice
27. call a parent class's method from child class in python
link:http://stackoverflow.com/questions/805066/call-a-parent-classs-method-from-child-class-in-python
28. how do i execute a program from python os.system fails due to spaces in path
import subprocess
subprocess.call(['ls','-al'])
29. tabs versusspaces in python programming
30. python removing duplicates in lists
t = [1, 2, 3, 1, 2, 5, 6, 7, 8]
print list(set(t))
31. how to change a string into uppercase
string.upper()
32. how can i imporove my paw detection
link:http://stackoverflow.com/questions/4087919/how-can-i-improve-my-paw-detection
33. a transpose/unzip function inpython (inverse of zip)
original = [('a', 1), ('b', 2), ('c', 3), ('d', 4)]
print zip(*original)
34. good pdf report generator tool for python
link:http://stackoverflow.com/questions/177799/good-pdf-report-generator-tool-for-python
35. is there a simple, elegant way to define singletons in python
link:http://stackoverflow.com/questions/31875/is-there-a-simple-elegant-way-to-define-singletons-in-python
36. how to capitalize the first letter of each word in a string
print u'hello world'.title()
37. python: if/else in list comprehension
link:http://stackoverflow.com/questions/4260280/python-if-else-in-list-comprehension
38. how to get the filename without extension from a path in python
link:http://stackoverflow.com/questions/678236/how-to-get-the-filename-without-the-extension-from-a-path-in-python
39. representing and solving a maze given an image
link:http://stackoverflow.com/questions/12995434/representing-and-solving-a-maze-given-an-image
40. generate random integes between 0 and 9
from random import randint
print randint(0,9)
41. python: user input and commandline arguments
link:http://stackoverflow.com/questions/70797/python-user-input-and-commandline-arguments
42. python interger incrementing with ++
b = 3
b += 1
43. No module named Mysqldb
easy_install mysql-python (mix os)
pip install mysql-python (mix os)
apt-get install python-mysqldb
yum instal mysql-python
44. python style:multiple-line conditions in ifs
link:http://stackoverflow.com/questions/181530/python-style-multiple-line-conditions-in-ifs
45. getting the correct encoding when piping stdout in python
link:http://stackoverflow.com/questions/492483/setting-the-correct-encoding-when-piping-stdout-in-python
46. heavy usage of python at google
47. can i use python as bash replacement
link:http://stackoverflow.com/questions/209470/can-i-use-python-as-a-bash-replacement
49. what is setup.py
python seup.py install
50. python -intersection of two lists
link:http://stackoverflow.com/questions/642763/python-intersection-of-two-lists
