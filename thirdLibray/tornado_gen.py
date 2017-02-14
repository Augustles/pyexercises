# coding=utf-8

import time
from tornado import ioloop, gen
now = time.time()
import requests

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
def main():
    if True:
        ret = yield [master(x) for x in xrange(999)]
        for y in ret:
            print y
        # for x in xrange(99):
            # print 'main start %s...' %x
            # ret = yield master(x)
            # print ret

ioloop.IOLoop.current().run_sync(main)
