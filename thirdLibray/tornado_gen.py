# coding=utf-8


from pymongo import MongoClient
from fabric.colors import green, red
import time
from tornado import ioloop, gen

DBINFO = 'mongodb://august:nana@0.0.0.0:27017/'

nbbs = MongoClient(DBINFO).nbbs.tmp


nzol = nbbs.find().batch_size(61)
now = time.time()


@gen.coroutine
def worker1(url):
    pass


@gen.coroutine
def worker(cmd, p):
    # print(green(cmd))
    yield worker1(cmd)


@gen.coroutine
def master(item):
    # print(red(item))
    yield worker(item, 0)


@gen.coroutine
def main():
    update = []
    if not update:
        for item in nzol:
            yield master(item)

    end = time.time()
    print(red('spend {0} mins'.format((end - now) / 60)))


try:
    ioloop.IOLoop.current().run_sync(main)
except Exception as e:
    print(red(e))
