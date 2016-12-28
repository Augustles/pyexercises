# coding=utf-8

import time
from tornado import ioloop, gen
now = time.time()
import requests

@gen.coroutine
def worker(item):
    r = requests.get('http://www.baidu.com')
    print 'worker done %s url: %s , status: %s' %(item,r.url,r.status_code)


@gen.coroutine
def master(item):
    print 'master done %s' %item
    yield worker(item)


@gen.coroutine
def main():
    if True:
        for x in xrange(99):
            print 'main start ...'
            yield master(x)

try:
    ioloop.IOLoop.current().run_sync(main)
except Exception as e:
    print e
