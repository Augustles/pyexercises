# coding=utf-8

import time
from tornado import ioloop, gen
import requests
import multiprocessing

now = time.time()
info = range(37)

def cost():
    def wrap(fun):
        def sub_wrap(*args, **kw):
            res = None
            t2 = time.time()
            res = fun(*args, **kw)
            cost = time.time() - t2
            print(res, fun.__name__, args, kw, cost)
            return res
        return sub_wrap
    return wrap

@gen.coroutine
def worker(item):
    r = requests.get('http://www.baidu.com')
    raise gen.Return('worker done %s url: %s , status: %s' %(item,r.url,r.status_code))


@gen.coroutine
def master(item):
    # print 'master done %s' %item
    ret = yield worker(item)
    # 可以用gen.Return返回yield
    raise gen.Return(ret)


@gen.coroutine
def main(item):
    for x in item:
        res = yield master(x)
        print res



@cost()
def run_ioloop(x):
    try:
        # 向run_sync传递参数
        ioloop.IOLoop.current().run_sync(lambda: main(x))
    except Exception as e:
        print e.message

start, end = 0, 0

# 多进程+协程
# for x in range(4):
    # start = end
    # end += int(round(len(info) / 4.0))
    # print start, end
    # # 多进程
    # p = multiprocessing.Process(target=run_ioloop, args=(info[start: end],))
    # p.start()
    # p.join()

from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor

# 异步调用同步函数
class Async(object):
    def __init__(self):
        self.executor = ThreadPoolExecutor(3)

    @run_on_executor
    @cost()
    def test(cls, x):
        time.sleep(x)
        print(x)

    @gen.coroutine
    @run_on_executor
    def test2(cls, x):
        time.sleep(0.15)
        print(x, 'hi')

    @run_on_executor
    @cost()
    def run_ioloop(cls, x):
        try:
            ioloop.IOLoop.current().run_sync(lambda: cls.test2(x))
        except Exception as e:
            print e.message

@gen.coroutine
def start_pro(x):
    a = Async()
    yield [a.test(x), a.test2(x)]

b = Async()
b.run_ioloop(info)
# for x in range(5):
    # ioloop.IOLoop.current().run_sync(lambda: start_pro(x))
