

stackoverflow vote top 201~251

201. how do i 'cd' in python
import os
os.chdir('d:/')
202. string comparison in python:is vs.  ==  同上
203. should i use urllib or urllib2 or requests   requests
204. get last day of the month in python
import calendar
print calendar.monthrange(2015, 6)[1]
205. converting a string to dictionary
s = "{'muffin' : 'lolz', 'foo' : 'kitty'}"
import ast
print ast.literal_eval(s)
206. difference between abstract class and interface in python
link:http://stackoverflow.com/questions/372042/difference-between-abstract-class-and-interface-in-python
207. where do the python until tests go
link:http://stackoverflow.com/questions/61151/where-do-the-python-unit-tests-go
208. what's the best solution for openid with django
209. unstanding kwargs in pyhon   同上
210. proper indentation for python multiline strings   ()
211. python split strings with multiple delimiters
import re
data = "Hey, you - what are you doing here!?"
print re.findall(r'[\w]+', data)
212. use a glob() to find files recursively in python
link:http://stackoverflow.com/questions/2186525/use-a-glob-to-find-files-recursively-in-python
import fnmatch
import os
matches = []
for root, dirnames, filenames in os.walk('.'):
    print root,dirnames,filenames
213. retrieving python module path
print os.__file__,re.__file__
214. not None test in python
if data is not None:print 1
215. delete an element from dictionary   del dict[key]
216. python's use of __new__ and __init__
217. python __slot__
限制实例的属性
218. what is a python egg   python中的包
219. how do you get the logical xor of two variables in python
link:http://stackoverflow.com/questions/432842/how-do-you-get-the-logical-xor-of-two-variables-in-python
220. python flask vs. bottle   flask
221. python try-else
try:
    2/0
except Exception, e:
    print e
222. best practice for python assert   断点
223. build a basic python iterator
link:http://stackoverflow.com/questions/19151/build-a-basic-python-iterator
224. django development ide   pycharm vim sublime
225. disable output buffering
link:http://stackoverflow.com/questions/107705/disable-output-buffering
226. django -setup a scheduled job
link:http://stackoverflow.com/questions/573618/django-set-up-a-scheduled-job
227. how to get the function name as string in python
print os.__name__,re.__name__
228. how to parse iso formatted date in python
link:http://stackoverflow.com/questions/127803/how-to-parse-iso-formatted-date-in-python
229. finding local ip addresses using python's stdlib
import socket
print socket.gethostbyname(socket.gethostname())
230. how to detect whether a python variable is a function
hasattr(obj, '__call__')
231. remove empty strings from a list of strings
str_list = filter(None, str_list) # fastest
str_list = filter(bool, str_list) # fastest
232. converting unix timestamp string to readable date in python
import datetime
unix_time = "1284101485"
print datetime.datetime.fromtimestamp(int(unix_time)).strftime('%Y-%m-%d %H:%M:%S')
233. argparse optional positional arguments
link:http://stackoverflow.com/questions/4480075/argparse-optional-positional-arguments
234. showing the stack trace from a running python application
link:http://stackoverflow.com/questions/132058/showing-the-stack-trace-from-a-running-python-application
235. how can i use python to get the system hostname
print socket.gethostname()
236. what is the naming convertion in python for variable and function names
link:http://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names
237. how can i get concatenation of two lists in python without modifying either one
238. what is a python equivalent of php's var_dump()
import pprint
pprint.pprint(globals())
pprint.pprint(locals())
239. open in python does not create a file if it doesn't if it doesn't exist
fp = open('test.txt', 'w+')
240. how do you express binary literals in python   bin() oct() hex()
241. flattening a shallow list in python
t = [['image00', 'image01'], ['image10'], []]
l2 = [y for x in t for y in x];print l2
import itertools
chain = itertools.chain(*t);print list(chain)
242. what is the python equivalent of static variables inside a function
link:http://stackoverflow.com/questions/279561/what-is-the-python-equivalent-of-static-variables-inside-a-function
243. why are some float <integer comparisons four times slower than others
link:http://stackoverflow.com/questions/30100725/why-are-some-float-integer-comparisons-four-times-slower-than-others
244. time.sleep -- sleeps thread or process   import time time.sleep(1)
245. display number with leading zeros
print '0{0}'.format(1,)
246. why is 'x' in ('x',) faster than 'x' == 'x'
link:http://stackoverflow.com/questions/28885132/why-is-x-in-x-faster-than-x-x
247. a clean lightweight alternative to python's twisted
248. python equivalent of && in an if statement   and &&
249. fastest way to list primes below N
link:http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n
