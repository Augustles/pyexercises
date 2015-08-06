
stackoverflow vote top

1. python pip install fials:invalid command egg_info
2. how to manage local vs. production settings in django
3. practicing bdd with python
http://stackoverflow.com/questions/231371/practicing-bdd-with-python
4. what does the at (@) symbol do in python
@ is symbol decorators used for class, function and method
5. what is the standard way to add N seconds to datetime.time in python
from datetime import datetime, timedelta
now = datetime.now()
c = timedelta(seconds=3) # hours,days,years,minutes,weeks,microsecond,millisecond
tNow=now + c
print now,tNow
6. what is a 'callable' in python
http://stackoverflow.com/questions/111234/what-is-a-callable-in-python
7. how to set the current working directory in python
os.chdir(path)
8. how can i get alist of all classes within current module in python
http://stackoverflow.com/questions/1796180/how-can-i-get-a-list-of-all-classes-within-current-module-in-python
9. why do you have to call .iteritems() when itering over a dictionary in python
d.items(),d.iteritems(),d.keys(),d.iterkeys(),d.values(),d.itervalues()
10. python list of lists, changes reflected across sublists unexpectedly
t = [[1]*4 for n in range(3)]
t[1][1] = 9;print(t)
11. remove all occuences of a value from a python list
x = [1,2,3,2,2,2,3,4]
print(filter(lambda x: x != 2, x))
12. python:read password from stdin
import getpass
pw = getpass.getpass('please enter you password')
13. how do i execute a sting containing python code in python
mycode = 'print "hello world"'
exec mycode
x = eval('2*7');print(x)
14. python git module experiences
http://stackoverflow.com/questions/1456269/python-git-module-experiences
15. how can i tell pycharm what type a parameter is expected to be
http://stackoverflow.com/questions/6318814/how-can-i-tell-pycharm-what-type-a-parameter-is-expected-to-be
16. how do i filter foreignkey choices in a django modelform
http://stackoverflow.com/questions/291945/how-do-i-filter-foreignkey-choices-in-a-django-modelform
17. why is it slower to iterate over a small string than a small list
http://stackoverflow.com/questions/23861468/why-is-it-slower-to-iterate-over-a-small-string-than-a-small-list
18. is there a numpy function to return the first index of something in an array
http://stackoverflow.com/questions/432112/is-there-a-numpy-function-to-return-the-first-index-of-something-in-an-array
19. how can i check the syntax of python script without executing it
python -m py_compile test.py, python -O -m compileall path   convert to .pyo
20. how do i translate a iso 8601 datetime string into a python datetime object
b = "2015-03-04T21:08:12"
obj_time = datetime.strptime(b, '%Y-%m-%dT%H:%M:%S');print obj_time
21. moving a file in python
os.rename(old_path, new_path), shutil.move(old_path, new_path)
22. remove specific characters from a string in python
import re
line = 'abd,asd,@#$'
line = line.translate(None, '#$');print(line)
print(re.sub('[,#@]','', line))
23. short description of python scoping rules
http://stackoverflow.com/questions/291978/short-description-of-python-scoping-rules
24. what exactly do 'u' and 'r' string flags do in python,and what are raw stringliterals
u'strings' is unicode, r is raw string, 不会转义路径\字符
25. what is the difference between python's re.search and re.match
http://stackoverflow.com/questions/180986/what-is-the-difference-between-pythons-re-search-and-re-match
26. how to find out if a python object a string
isinstance(obj, basestring)
27. python try...except comma vs. 'as' in except
try:
    1/0
except Exception as e: # except Exception, e:
    print e
28. sleeping in a batch file   批处理文件
sleep 5
http://stackoverflow.com/questions/166044/sleeping-in-a-batch-file
29. python:split string with multiple delimiters
string.split() import shlex shlex.split()
a='Beautiful, is; better*than\nugly'
print re.split(',|;|\*|\n', a)
30. what is the python keyword 'with' used for
http://stackoverflow.com/questions/1369526/what-is-the-python-keyword-with-used-for
31. reducing django memory usage.low hanging fruit
http://stackoverflow.com/questions/487224/reducing-django-memory-usage-low-hanging-fruit
32. convert all strings in a list to int
results = ['1', '2', '3']
r = map(int, results);print r
33. databaseerror:current transaction is aborted,commands ignored until end of transaction block
http://stackoverflow.com/questions/2979369/databaseerror-current-transaction-is-aborted-commands-ignored-until-end-of-tra
34. separation of business logic and data access in django
http://stackoverflow.com/questions/12578908/separation-of-business-logic-and-data-access-in-django
35. lazy method for reading big file in python
http://stackoverflow.com/questions/519633/lazy-method-for-reading-big-file-in-python
36. why (0-6) is -6 False
http://stackoverflow.com/questions/11476190/why-0-6-is-6-false
37. how do you log server errors on django sites
http://stackoverflow.com/questions/238081/how-do-you-log-server-errors-on-django-sites
38. how can i parse a yaml file
http://stackoverflow.com/questions/1773805/how-can-i-parse-a-yaml-file
39. why is early return slower than else
http://stackoverflow.com/questions/8271139/why-is-early-return-slower-than-else
40. filter dict to contain only certain keys
unwanted = set(keys) -set(your_dict)
41. python + django page redirect
http://stackoverflow.com/questions/523356/python-django-page-redirect
42. can i install python windows packages into virtualenvs
easy_install package pip install package
43. turn a string into valid filename in python
http://stackoverflow.com/questions/295135/turn-a-string-into-a-valid-filename-in-python
44. why does ~ True result in -2
print(~1) # True is 1
http://stackoverflow.com/questions/21881362/why-does-true-result-in-2
45. can a variable number of arguments be passed to a function
http://stackoverflow.com/questions/919680/can-a-variable-number-of-arguments-be-passed-to-a-function
46. store output of subprocess.Popen call in a string
import subprocess
out = subprocess.check_output('ls')
47. python documentation generator
http://stackoverflow.com/questions/1125970/python-documentation-generator
48. how can i compare two lists in python and return matches
http://stackoverflow.com/questions/1388818/how-can-i-compare-two-lists-in-python-and-return-matches
a = [1, 2, 3, 4, 5]
b = [9, 8, 7, 6, 5]
print(set(a) & set(b)) # 交集
print(set(a) ^ set(b)) # 非共同
print(set(a)-set(b)) # 只存在a的
print(set(b)-set(a)) # 只存在b的
print(set(a)+set(b)) # 并集
49. split string into list in python
string.split() a.apped(x)
50. what is the best way to implement nested dictionaries in python
http://stackoverflow.com/questions/635483/what-is-the-best-way-to-implement-nested-dictionaries-in-python


