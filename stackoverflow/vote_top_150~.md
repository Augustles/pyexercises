
stackoverflow 101~150

101. ascii value of a character in python
print ord('a'),chr(97),unichr(97),type(unichr(97))
102. why shoudn't use pypy over cpython if pypy is 6.3 times faster
103. how can i get a list of locally installed python modules
import pip
installed_list = sorted(["%s==%s" %(i.key,i.version) for i in pip.get_installed_distributions()])
print installed_list
104. why [] faster than list()
105. what's the difference between list and tuples
Tuples have structure, lists have order.
106. how to remove an element from a list by index in python
lst1 = range(3,9) # lst1.remove(value)
del lst1[2]
107. speed comparison with project euler: c vs python vs erlang vs haskell
108. how do i parse xml in python
import xml
e = xml.etree.ElementTree.parse('test.xml').getroot()
for type_a in e.findall('type'):
    print type_a.get('foobar')
109. python @property versus getters and setters
110. converting integer to string in python   str(), int()
111. why python lambda are useful
112. what are 'named tuples' in python
113. how to determine the variable type in python   type() isinstance()
114. drectory listing in python
import os
for dirname, dirnames,filenames in os.walk('.'):
    print dirname,dirnames,filenames
    # for filename in filenames:
    #     print os.path.join(dirname,filename)
115. how can i do a line break (line continuation) in python
str1 = ('1' + '2' + '3' +
    '4' + '5')
a = '1' + '2' + '3' + \
    '4' + '5'
116. why does comparing strings in python using either '==' or 'is' somtimes is different result
'is'相当于object对象的判断id,==是value的判断
117. installing pip on mac os x
brew install python   pip will work
118. how to get file creation & modification date/times in python
import os.path, time
print "last modified: %s" % time.ctime(os.path.getmtime('.'))
print "created: %s" % time.ctime(os.path.getctime('.'))
119. pip install mysql-python fails with environmenterror:mysql_config not found
apt-get install libmysqlclient-dev python-dev
120. use different python version with virtualenv   vitualenv & virtualenvwrapper
virtualenv -p /usr/bin/python2.6 <path/to/new/virtualenv/>
121. what do people write #!/usr/bin/env python on the python on the first line of a python script
122. how can i caount the occurrences of a list item in python
x = range(3,9) + [3,7,3,3,9,3]
print x.count(3)
123. python multithreading for dummies
link:http://stackoverflow.com/questions/2846653/python-multithreading-for-dummies
124. python setup.py uninstall
python setup.py install --record files.txt
cat files | xrags rm -rf
link:http://stackoverflow.com/questions/1550226/python-setup-py-uninstall
125. how do i protect python code
link:http://stackoverflow.com/questions/261638/how-do-i-protect-python-code
126. limiting floats to two decimal points
print '{0:.3f}'.format(13.949999988079071)
127. mkdir -p funtionality in python
link:http://stackoverflow.com/questions/600268/mkdir-p-functionality-in-python
128. how to get line count cheaply in python
num_lines = sum(1 for line in open('vote_top_101_150.py'));print num_lines
129. terminating a python script   终止
import sys,os
sys.exit()
130. how to acess environment varibles from python
print sys.prefix,os.environ
131. if python is interpreted,what are .pyc files
link:http://stackoverflow.com/questions/2998215/if-python-is-interpreted-what-are-pyc-files
132. how do i download a file over http using python
link:http://stackoverflow.com/questions/22676/how-do-i-download-a-file-over-http-using-python
133. how to import a module given the full path
import imp
foo = imp.load_source('module.name', '/path/to/file.py')
foo.MyClass()
134. is there a function in python to print all the current properties and values of an object
link:http://stackoverflow.com/questions/192109/is-there-a-function-in-python-to-print-all-the-current-properties-and-values-of
from pprint import pprint
pprint(vars(__builtins__))
135. how can i tell if a string repeats itself in python
http://stackoverflow.com/questions/29481088/how-can-i-tell-if-a-string-repeats-itself-in-python
136. how do i check what version of python is running my script
sys.version
137.'has_key()' or 'in'   in
138. is there any way to kill a thread in python
link:http://stackoverflow.com/questions/323972/is-there-any-way-to-kill-a-thread-in-python
139. json datetime between python and javascript
link:http://stackoverflow.com/questions/455580/json-datetime-between-python-and-javascript
140. behaviour of increment and decrement operators in python   ++count  a += 1
link:http://stackoverflow.com/questions/1485841/behaviour-of-increment-and-decrement-operators-in-python
141. multiline commet in python   多行注释
142. convert hex string int in python
int(hex(11),16), int(oct(22),8)
143. should you always favor xrange() over ranger()   range()
144. what is a clean,pythonic way to have multiple construtors in python
link:http://stackoverflow.com/questions/682504/what-is-a-clean-pythonic-way-to-have-multiple-constructors-in-python
146. how do you remove duplicates from a list in python whilst preserving order
link:http://stackoverflow.com/questions/480214/how-do-you-remove-duplicates-from-a-list-in-python-whilst-preserving-order
147. remove items from a list while iterating in python
148. how do i delete a file or folder in python
os.remove(fp) will remove a file
os.rmdir(fp) will remove an empty dirctory
shutil.rmtree(dir) will delete a dir and its all contents
149 what is the best project structure for a python application
link:http://stackoverflow.com/questions/193161/what-is-the-best-project-structure-for-a-python-application
150. convert bytes to a python string
link:http://stackoverflow.com/questions/606191/convert-bytes-to-a-python-string
151. how do i check if a variable exists in python
if 'var' in locals():print 1
if 'var' in globals():print 1
if hasattr(obj,'attr_name'):print 1
