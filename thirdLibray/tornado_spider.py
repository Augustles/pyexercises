# coding=utf-8

from datetime import timedelta
from bs4 import BeautifulSoup
from tornado.httpclient import AsyncHTTPClient
from tornado import ioloop, gen, queues
import time


@gen.coroutine
def fetch(url):
    print('fetcing', url)
    # 这是一个异步的请求
    response = yield AsyncHTTPClient().fetch(url, raise_error=False)
    raise gen.Return(response)

_q = queues.Queue()

@gen.coroutine
def run():
    try:
        # 取得url
        url = yield _q.get()
        # 进行异步fetch
        # 返回结果, 不是用return, 用的是raise gen.Return
        res = yield fetch(url)
        html = res.body
        if html:
            soup = BeautifulSoup(html, 'lxml')
            print 'url: %s title: %s' %(url, soup.find('title'))
    finally:
        _q.task_done()


@gen.coroutine
def worker():
    while not _q.empty():
        yield run()


@gen.coroutine
def main():
    for i in range(73000, 74100):    # 放100个链接进去
        url = "http://www.jb51.net/article/%d.htm" % i
        yield _q.put(url)
    for _ in range(100):    # 模拟100个线程
        worker()
    yield _q.join()
    # yield _q.join(timeout=timedelta(seconds=30))


if __name__ == '__main__':
    start = time.time()
    # 返回future对象
    # future和gevent中Waiter对象相类似,
    # gevent Waiter switch通过设置其greenlet属性切换到向主hub loop
    # Waiter就是用于切换不同greenlet到主hup loop
    # future是一个穿梭于协程和调度器(ioloop)的信使
    # 提供回调函数注册(当异步任务完成后,调用回调)
    # runner保存中间结果,唤醒父协程等功能
    # 如果说tornado是一辆车,那么runner对象就是他的发动机
    # 每一个协程都是由一runner实例完成的
    ioloop.IOLoop.current().run_sync(main)
    print 'spend %.3f' %(time.time()-start)
