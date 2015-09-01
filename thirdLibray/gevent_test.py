# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey; monkey.patch_all()
# 修改Python自带的一些标准库
import gevent
from gevent.pool import Group
import grequests
import requests


def f(url):
    # reqs = [grequests.get(l) for l in url]

    r = requests.get(url)
    print('GET: {0} {1}'.format(r.status_code,r.url))

l = ['https://www.yahoo.com/','http://www.baidu.com/','https://www.python.org/']

# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'http://www.baidu.com/'),
# ])
greenlets = [gevent.spawn(f, x) for x in l]
gevent.joinall(greenlets)

for x in l:
    f(x)
def g(l):
    for x in l:
        group = Group()
        group.apply_async(f,args=(x,))
        # group.add(gevent.spawn(f,x))
        group.join()
# g(l)
def g4(l):
    g = Group()
    g.map_async(f, l).get()
# g4(l)




