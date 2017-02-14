# coding=utf-8

from tornado import gen, ioloop
import requests
from time import time

headers = {
    'UserAgent': 'Googlespider',
}
@gen.coroutine
def worker(qs):
    r = requests.get(qs, headers=headers)
    soup = bs(r.content, 'lxml')
    info = soup.find('div', attrs={'class': 'timeline'}),find_all('li', attrs={'data-item-type': 'tweet'})
    for x in info:
        print x

@gen.coroutine
def main():
    start = 'https://mobile.twitter.com/yua_mikami'
    res = yield worker(start)
    print res

if __name__ == '__main__':
    st = time()
    ioloop.IOLoop.current().run_sync(main)
    print 'spend %.3f' %(time()-st)
