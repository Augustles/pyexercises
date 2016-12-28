# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from gevent import monkey
monkey.patch_all()
# 修改Python自带的一些标准库
import gevent
from gevent.pool import Group, Pool
# import grequests
import requests
import time

# 协程可以中断, 然后再执行


start = time.time()
def f(url):
    # reqs = [grequests.get(l) for l in url]

    print 'ok'
    r = requests.get(url)
    gevent.sleep()  # 切换回到主loop协程中, 通知主coroutine当前的coroutine已经block
    print('GET: {0} {1}'.format(r.status_code, r.url))

l = ['https://www.yahoo.com/',
     'http://www.baidu.com/',] * 30

gevent.joinall([ gevent.spawn(f, g) for g in l])

print time.time()-start
# 在任何时刻, 有且只有一个协程在运行
# 这里是初始化一个greenlet, 并向注册到主hub loop, 需要hub.swith()才会调用
# test = gevent.spawn(f, l[0])

# 实际上是调用Waiter.switch
# Waiter对象有一个greenlet属性,表明当前这个waiter属于那个greenlet
# Waiter.get方法设置greelet属性,并切换到hub loop(run)
# gevent.sleep()

def hi():
    print 'hi'

# 这里类似上面的spawn, sleep
# gevent.get_hub().loop.run_callback(hi)
# gevent.get_hub().loop.run()


# pool = Pool(4)  # 使用pool管理协程数目
# import time
# greenlets = [gevent.spawn(f, x) for x in l]  # gevent.spaw已经(注册到主hub loop)开始执行协程, 初始化了greenlet对象, 调用start()
# result = gevent.joinall(greenlets)  # 把greenlet结果收集起来
# print result


# def g(l):
    # for x in l:
        # group = Group()
        # group.apply_async(f, args=(x,))
        # # group.add(gevent.spawn(f,x))
        # group.join()
# # g(l)


# def g4(l):
    # g = Group()
    # g.map_async(f, l).get()
# g4(l)


# import random
# from time import sleep
# from greenlet import greenlet
# from Queue import Queue

# queue = Queue(1)

from greenlet import greenlet

# def a():
    # aa = 12
    # print aa
    # b.switch()
    # bb = 34
    # print bb
    # b.switch()

# def b():
    # cc = 56
    # print cc
    # a.switch()
    # dd = 78
    # print dd

# a = greenlet(a)
# b = greenlet(b)
# a.switch()
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
