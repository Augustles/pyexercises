
stackoverflow top 450~

1. when is 'i += x' different from 'i = i + x' in python
link:http://stackoverflow.com/questions/15376509/when-is-i-x-different-from-i-i-x-in-python
2. why is there no GIL in java virtual machine why does python need one so bad
link:http://stackoverflow.com/questions/991904/why-is-there-no-gil-in-the-java-virtual-machine-why-does-python-need-one-so-bad
3. how to check if type of a variable is string in python
link:http://stackoverflow.com/questions/4843173/how-to-check-if-type-of-a-variable-is-string-in-python
4. reading binary file in pythotn
link:http://stackoverflow.com/questions/1035340/reading-binary-file-in-python
5. django-what is the difference between render(),render_to_response() and direct_to _template()
link:http://stackoverflow.com/questions/5154358/django-what-is-the-difference-between-render-render-to-response-and-direc
6. python urlencode string
link:http://stackoverflow.com/questions/5607551/python-urlencode-string
7. why use python's os module methods instead of execting shell commands directly
link:http://stackoverflow.com/questions/28572833/why-use-pythons-os-module-methods-instead-of-executing-shell-commands-directly
8. get md5 hash of big files in python
link:http://stackoverflow.com/questions/1131220/get-md5-hash-of-big-files-in-python
9. class method differeces in python:bound,unbound and static
link:http://stackoverflow.com/questions/114214/class-method-differences-in-python-bound-unbound-and-static
10. what's the idiomatic syntax for prepending to a short python list
l = range(2,9)
l.insert(0,11);print l
11. python list vs. array when to use
link:http://stackoverflow.com/questions/176011/python-list-vs-array-when-to-use
12. how can i create a directly-executable cross-platform gui app using python
link:http://stackoverflow.com/questions/2933/how-can-i-create-a-directly-executable-cross-platform-gui-app-using-python
13. why wasn't pypy included in standard python
link:http://stackoverflow.com/questions/12867263/why-wasnt-pypy-included-in-standard-python
14. how to get full path of current file's directory in python
15. how do i remove the first item from python list
l.pop(0)
del l[0];print l
16. pg_config executable not found
link:http://stackoverflow.com/questions/11618898/pg-config-executable-not-found
17. c-like structures in python
from collections import namedtuple
Mystruct = namedtuple('Mystruct', 'field1 field2 field3')
m =  Mystruct('foo','jim','tom')
print m.field3
18. circular (or cyclic) imports in python
link:http://stackoverflow.com/questions/744373/circular-or-cyclic-imports-in-python
19. overloading __init__ in python
link:http://stackoverflow.com/questions/141545/overloading-init-in-python
20. how to empty list in python
del l[:]
l[:] = []
21. how do i make python to wait for a pressed key 触碰某个键才会继续进行
import msvcrt
def wait():
    msvcrt.getch()
22. how do i resize an image using pil and maintain its aspect ratio
link:http://stackoverflow.com/questions/273946/how-do-i-resize-an-image-using-pil-and-maintain-its-aspect-ratio
23. how do i watch a file for changes using python
link:http://stackoverflow.com/questions/182197/how-do-i-watch-a-file-for-changes-using-python
24. why use arparse rather than optparse
link:http://stackoverflow.com/questions/3217673/why-use-argparse-rather-than-optparse
25. difference between __getattr__ vs. __getattribute
link:http://stackoverflow.com/questions/3278077/difference-between-getattr-vs-getattribute
26. python remove all whitespace in a string
string.strip(),string.replace()
27. python mysqldb:library not loaded:libmysqlclient.18.dylib
link:http://stackoverflow.com/questions/6383310/python-mysqldb-library-not-loaded-libmysqlclient-18-dylib
28. is there any way to do http put in python
link:http://stackoverflow.com/questions/111945/is-there-any-way-to-do-http-put-in-python
29. choosing java vs. python on google app engine
link:http://stackoverflow.com/questions/1085898/choosing-java-vs-python-on-google-app-engine
30. python open built-in function:difference between modes a,a+,w,w+,and r+
link:http://stackoverflow.com/questions/1466000/python-open-built-in-function-difference-between-modes-a-a-w-w-and-r
31. which exception should i raise on bad/illegal argument combinations in python
link:http://stackoverflow.com/questions/256222/which-exception-should-i-raise-on-bad-illegal-argument-combinations-in-python
32. python:list vs. tuple,when to use each
link:http://stackoverflow.com/questions/1708510/python-list-vs-tuple-when-to-use-each
33. mysql_config not found when installing mysqldb python interface
link:http://stackoverflow.com/questions/7475223/mysql-config-not-found-when-installing-mysqldb-python-interface
34. generator expressions vs. list comprehension
一般用列表解析,相应的还有词典解析,生成表达式
35. how to define two-dimensional array in python
m = [[0 for x in range(5)] for x in range(5)] 
m[0][2] = 3
m[1][3] = 6
print m,type(m)
36. check if a given already exists in a dictionary and increment it
link:http://stackoverflow.com/questions/473099/check-if-a-given-key-already-exists-in-a-dictionary-and-increment-it
37. understanding __get__ and __set__ and python descriptors
link:http://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors
38. how to get time of a python program execution
import time
st = time.time()
time.sleep(5)
end = time.time()
f = (end-st)/60
print 'spend {0:.3f} mins'.format(f)
39. how to read large file,line by line in python
with open('test.log') as f:
    for line in f:
        pass
40. python:replace charaters in string
to_remove = [',','.','!','?']
t = 'A.B!C?D'
print t.translate(None,''.join(to_remove))
t1 = ''.join([x for x in t if x not in to_remove])
print t1
41. what does the python ellipsis object do
ink:http://stackoverflow.com/questions/772124/what-does-the-python-ellipsis-object-do
42. why numpy instead of python lists
link:http://stackoverflow.com/questions/993984/why-numpy-instead-of-python-lists
43. indentationerror:unindent does not match
link:http://stackoverflow.com/questions/492387/indentationerror-unindent-does-not-match-any-outer-indentation-level
44. how can i find sript's diretory with python
os.path.dirname()   os.path.split()   os.path.splitext() 分割为拓展名
45. how to print full traceback without halting the program
link:http://stackoverflow.com/questions/3702675/how-to-print-the-full-traceback-without-halting-the-program
import traceback
import sys
try:
    pass
except Exception, err:
    print traceback.format_exc()
    print sys.exc_info([0])
46. how can i color python logging output
link:http://stackoverflow.com/questions/384076/how-can-i-color-python-logging-output
47. python how do i pass a string into subprocess.Popen()
link:http://stackoverflow.com/questions/163542/python-how-do-i-pass-a-string-into-subprocess-popen-using-the-stdin-argument
48. what is the purpose of the single underscore '_' variable in python
link:http://stackoverflow.com/questions/5893163/what-is-the-purpose-of-the-single-underscore-variable-in-python
49. how do i sort a list of strings in python
l.sort()   sorted()
