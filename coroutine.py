# coding=utf-8


# 协程
import time
import re
from bs4 import BeautifulSoup as bs
import requests
import os

# def consumer():
#     r = ''
#     while True:
#         # 接收produce的n值,并传递r值
#         url = yield r
#         # if not n:
#         #     return
#         print('[CONSUMER] consuming %s...' % url)
#         time.sleep(1)
#         r = requests.get(url)
#         r = r.status_code

#         # r = '200 OK'

# def produce(c):
#     '''x.next() -> the next value'''
#     c.next() # next启动进入consumer的生成器
#     links = []
#     n = 0
#     f = range(0,300,25)
#     for n in f:
#         num = 'start='+ str(n)
#         url = re.sub(r'start\=\d+', num, doulists)
#         links.append(url)

#     n = 0
#     print(len(links))
#     while n < len(links)/2+1:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         # 切换到consumer执行,consumer完成后,继续执行produce
#         '''
#         Docstring:
#         send(arg) -> send 'arg' into generator,
#         return next yielded value or raise StopIteration.
#         '''
#         # 发送n到生成器，返回yield实例next值
#         url = links[n]
#         # t = requests.get(url)
#         # t = t.status_code
#         # print(t)
#         r = c.send(url)
#         t = requests.get(links[n+1])
#         f = links[n+1]
#         print('{0},{1},{2}'.format(n,t.status_code,f))
#         print('[PRODUCER] Consumer return: %s' % r)
#         n = n+1


#     c.close() # 关闭生成器

# doulists = 'http://www.douban.com/doulist/38849533/?start=50&sort=seq&sub_type='

# produce(consumer())

# 协程主要体现在等待io，数据处理时候，然后处理其他执行体，再回来执行
# produce向consumer发送n值,
# consumer向produce发送r值,相互交换
# 先执行一段,然后在执行其他,再回来执行剩下代码
# 不共享其变量
# 注意到consumer函数是一个generator（生成器），把一个consumer传入produce后：

# 1. 首先调用c.next()启动生成器；
# 2. 然后，一旦生产了东西(n)，通过c.send(n)切换到consumer执行；
# 3. consumer通过yield拿到消息，处理，又通过yield把结果传回；
# 4. produce拿到consumer处理的结果，继续生产下一条消息；
# 5. produce决定不生产了，通过c.close()关闭consumer，整个过程结束。
# 整个流程无锁，由一个线程执行，produce和consumer协作完成任务，所以称为“协程”，而非线程的抢占式多任务。
# 最后套用Donald Knuth的一句话总结协程的特点：
# “子程序就是协程的一种特例。”


# def worker():
#     s = ''
#     while True:
#         x = yield s
#         with open(x,'r') as r:
#             for s in r:
#                 pass


# def master(c):
#     c.next()
#     l = []
#     for x in os.listdir('.'):
#         if os.path.isfile(x):
#             print x
#             s = c.send(x)
#             l.append(s)
#     c.close()

# master(worker())


import time

def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        time.sleep(1)
        r = '200 OK'

def produce(c):
    c.next()
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()

if __name__=='__main__':
    c = consumer()
    produce(c)



# import random
# from time import sleep
# from greenlet import greenlet
# from Queue import Queue

# queue = Queue(1)

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




