
standard library(标准库)

1. json和simplejson的区别
json在2.6加入,simplejson在2.4+,simplejson更新效率高
import simplejson
2.使用http下载一个文件
直接使用urllib
base_url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
import urllib
urllib.urlretrieve(base_url)
import requests
r = requests.get(base_url)
print len(r.content)
3. argparse可选位置参数

4.有什么方法可以获取系统当前用户名?
import getpass
print getpass.getuser()
5.在python如何解析xml

6.如何使用python创建一个guid
import uuid
print uuid.uuid1()
7.我该使用urllib/urllib2还是requests
推荐requests
8. python中是否存在可以打印对象所有属性和方法 
from pprint import pprint
pprint (vars(uuid))
print dir(uuid)
9.如何展示一个正在运行的python应用的推展踪迹


10. python中,有什么办法杀死一个进程

11. python中isinstance()和type()区别
isinstance()一般用于有继承关系类的判断

