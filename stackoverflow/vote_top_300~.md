
vote top 300~

1. how can i reverse a list in python   [:]
2. how do i capture sigint in python
link:http://stackoverflow.com/questions/1112343/how-do-i-capture-sigint-in-python
3. python class inherits object
link:http://stackoverflow.com/questions/4015417/python-class-inherits-object
4. how to get an absolute file path in python
import os
print os.path.abspath('vote_top_300~.py')
5. dynamic module import in python
link:http://stackoverflow.com/questions/301134/dynamic-module-import-in-python
6. python's 'is' operator behaves unexpectedly with ingers
link:http://stackoverflow.com/questions/306313/pythons-is-operator-behaves-unexpectedly-with-integers
7. how to generate all permulations of a list in python
link:http://stackoverflow.com/questions/104420/how-to-generate-all-permutations-of-a-list-in-python
8. python __init__ and self what do they do
9. how can i subtract a day from a python date
from datetime import datetime, timedelta
now = datetime.now()
c_now = now + timedelta(days=-1)

from time import time,localtime
now = time()
t_now = localtime(now - 60*60*24);print t_now.tm_mon,t_now.tm_mday
10. calling c/c++ from python   ctypes
what is the standard python docstring forma   ''' doc string '''
11. save plot to image file instead of displaying it using matplotlib
link:http://stackoverflow.com/questions/9622163/save-plot-to-image-file-instead-of-displaying-it-using-matplotlib-so-it-can-be
12 what is a 'slub' in django
link:http://stackoverflow.com/questions/427102/what-is-a-slug-in-django
13. pretty printing xml in python
link:http://stackoverflow.com/questions/749796/pretty-printing-xml-in-python
14. list filtering: list comprehension vs. lambda + filter
link:http://stackoverflow.com/questions/3013449/list-filtering-list-comprehension-vs-lambda-filter
15. command line arguments in python
link:http://stackoverflow.com/questions/1009860/command-line-arguments-in-python
16. iterating over a string
link:http://stackoverflow.com/questions/538346/iterating-over-a-string
17. what is the difference between dict.items() and dict.iteritems()
link:http://stackoverflow.com/questions/10458437/what-is-the-difference-between-dict-items-and-dict-iteritems
18. preferred  python unit-testing framwork
link:http://stackoverflow.com/questions/191673/preferred-python-unit-testing-framework
19. python decimal range() step value
link:http://stackoverflow.com/questions/477486/python-decimal-range-step-value
20. how do i read a text file into s string variable in python
with open ("data.txt", "r") as myfile:
    data=myfile.read().replace('\n', '')
21. how to pip install packages acoording to requirements.txt from a localdirectory
pip install -r /path/to/requirements.txt
22. best way to strip puntuation from a string in python
link:http://stackoverflow.com/questions/265960/best-way-to-strip-punctuation-from-a-string-in-python
23. attempted relative import in non-pakage even with __init__.py
link:http://stackoverflow.com/questions/11536764/attempted-relative-import-in-non-package-even-with-init-py
24. how can i sort a dictary by key
d = {x:y for (x,y) in zip(range(9,1,-2),range(2,7))}
d_key = sorted(d.items(), key=lambda x:x[0]);print d_key
25. no module named pkg_resources
link:wget https://bitbucket.org/pypa/setuptools/raw/bootstrap/ez_setup.py -O - | python
26 how to print numbers with commas as thousands separator
link:http://stackoverflow.com/questions/1823058/how-to-print-number-with-commas-as-thousands-separators
27. getting key with maximum value in dictionary
import operator
print max(d.items(), key=operator.itemgetter(0))[0]
28. traverse a list in reverse order in python   reversed()
29. how to print date in a regular format in python
link:http://stackoverflow.com/questions/311627/how-to-print-date-in-a-regular-format-in-python
30. proper way to use **kwargs in python
31. how to create a guid in python
import uuid
uuid.uuid1()
32. how do you convert a python time.struct_time object in to datetime object
from time import mktime
from datetime import datetime
dt = datetime.fromtimestamp(mk(struct_time))
33. how do i do a case insensitive string comparison in python
link:http://stackoverflow.com/questions/319426/how-do-i-do-a-case-insensitive-string-comparison-in-python
34. how to check for nan in python
link;http://stackoverflow.com/questions/944700/how-to-check-for-nan-in-python
35. is it worth using python's re.compile
link:http://stackoverflow.com/questions/452104/is-it-worth-using-pythons-re-compile
36. super() raises 'typeerror must be type, not clasobj' for new-style class
link:http://stackoverflow.com/questions/9698614/super-raises-typeerror-must-be-type-not-classobj-for-new-style-class
37. does python have 'private' variables in classes
link:http://stackoverflow.com/questions/1641219/does-python-have-private-variables-in-classes
38. commet out a python code block
link:http://stackoverflow.com/questions/4324558/whats-the-proper-way-to-install-pip-virtualenv-and-distribute-for-python
39. python image library fails with message 'decoder jpeg not available' -pil
link:http://stackoverflow.com/questions/8915296/python-image-library-fails-with-message-decoder-jpeg-not-available-pil
40. in python,how do i get the path and name of the file that is currently executing
link:http://stackoverflow.com/questions/50499/in-python-how-do-i-get-the-path-and-name-of-the-file-that-is-currently-executin
41. python module for converting pdf to text
link:http://stackoverflow.com/questions/25665/python-module-for-converting-pdf-to-text
42. what does functools.wraps do
link:http://stackoverflow.com/questions/308999/what-does-functools-wraps-do
43. getting “Error loading MySQLdb module: No module named MySQLdb” - have tried  previously posted solutions
link:http://stackoverflow.com/questions/2952187/getting-error-loading-mysqldb-module-no-module-named-mysqldb-have-tried-pre
39. what's the proper way to install pip,virtualevn,and distribute for python
brew install pip/pip3 sudo apt-get install python-pip
44. why are there no ++ and -- operators in python
link:http://stackoverflow.com/questions/3654830/why-are-there-no-and-operators-in-python
45. python:check if an object is a list or tuple (but not string)
assert not isinstance(range(3), basestring)
46. python reverse /inverse a mapping
inverse_d = {x:y for (y,x) in d.items()}
print inverse_d
47. good way to append to a string
link:http://stackoverflow.com/questions/4435169/good-way-to-append-to-a-string
48. how to i determine the size of an object in python
import sys
print sys.getsizeof(d)
a = 4;print sys.getsizeof(a)
