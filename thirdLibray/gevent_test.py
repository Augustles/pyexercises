# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey
monkey.patch_all()
# 修改Python自带的一些标准库
import gevent
from gevent.pool import Group, Pool
import grequests
import requests

# 协程可以中断, 然后再执行


def f(url):
    # reqs = [grequests.get(l) for l in url]

    r = requests.get(url)
    gevent.sleep()  # 回到主loop协程中, 通知主coroutine当前的coroutine已经block
    print('GET: {0} {1}'.format(r.status_code, r.url))

l = ['https://www.yahoo.com/',
     'http://www.baidu.com/', 'http://mnwg.net/'] * 6

# gevent.joinall([
#         gevent.spawn(f, 'https://www.python.org/'),
#         gevent.spawn(f, 'https://www.yahoo.com/'),
#         gevent.spawn(f, 'http://www.baidu.com/'),
# ])
pool = Pool(4)  # 使用pool管理协程数目
import time
greenlets = [gevent.spawn(f, x) for x in l]  # gevent.spaw已经开始执行协程
result = gevent.joinall(greenlets)  # 把greenlet结果收集起来
print result


def g(l):
    for x in l:
        group = Group()
        group.apply_async(f, args=(x,))
        # group.add(gevent.spawn(f,x))
        group.join()
# g(l)


def g4(l):
    g = Group()
    g.map_async(f, l).get()
# g4(l)


# import random
# from time import sleep
# from greenlet import greenlet
# from Queue import Queue

# queue = Queue(1)

from greenlet import greenlet

def a():
    aa = 12
    print aa
    b.switch()
    bb = 34
    print bb
    b.switch()

def b():
    cc = 56
    print cc
    a.switch()
    dd = 78
    print dd

a = greenlet(a)
b = greenlet(b)
a.switch()
# @greenlet
# def producer():
#     chars = ['a', 'b', 'c', 'd', 'e']
#     global queue
#     while True:
#         char = random.choice(chars)
#         queue.put(char)
#         print "Produced: ", char
#         sleep(1)
#         consumer.switch()

# @greenlet
# def consumer():
#     global queue
#     while True:
#         char = queue.get()
#         print "Consumed: ", char
#         sleep(1)
#         producer.switch()

# if __name__ == "__main__":
#     producer.run()
#     consumer.run()
