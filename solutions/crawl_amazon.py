# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs
import re
import time
# from gevent import monkey
# monkey.patch_all()

# from pymongo import MongoClient

# conn = MongoClient('localhost', 27017)
# db = MongoClient('localhost', 27017).amazon
# movie = MongoClient('localhost', 27017).amazon.movie

headers = {
    'User-Agent': '  Mozilla/5.0 (Windows NT 6.1; rv:42.0) Gecko/20100101 Firefox/42.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'en',
    'Connection': 'keep-alive',
    'DNT': 1,
}
all_items = []
items = {}

urls = []
for x in xrange(1, 10):
    urls.append(
        'https://www.amazon.com/s/ref=sr_pg_{0}?rh=n%3A172282%2Cn%3A%21493964%2Cn%3A1266092011%2Cn%3A172659%2Cp_36%3A0-199999%2Cp_n_feature_keywords_three_browse-bin%3A7688788011&page={1}&ie=UTF8'.format(x, x))


def proxies():
    ips = {}
    with open('ava_ip.txt', 'r') as f:
        for line in f:
            if line.strip():
                proxie = "http://{0}".format(line.strip())
                ips['http'] = proxie
    return ips


def request(url):
    ss = requests.session()
    # http://segmentfault.com/q/1010000000511783
    # ss.proxies = p
    ss.headers.update(headers=headers)
    r = ss.get(url, timeout=None, verify=True)
    return r


def check_request(url):
    r = request(url)
    # 确保200状态
    while 1:
        t = 0.25
        if r.ok:
            return r
        else:
            time.sleep(t)
            r = request(url)
        t += 0.25
        if t > 7:
            print ' ==> Bad!'


def get_amazon_item(url):
    amazon_items = {}
    # r = check_request(url)
    # soup = bs(r.text)
    # n = soup.find('span',attrs={'class':'pagnRA'})
    # print n.a.get('href')
    # try:
    #     all = soup.find('div', attrs={'id': re.compile(
    #         r"\w+Results"), 'class': True}).find_all('li')
    # except AttributeError:
    while 1:
        r = check_request(url)
        soup = bs(r.text, 'html.parser')
        t = 0.25
        try:
            all = soup.find('div', attrs={'id': re.compile(
                r"\w+Results"), 'class': True}).find_all('li', attrs={'id': re.compile(r"result\_\d+"), 'class': True, 'data-asin': True})
            if all:
                break
        except AttributeError:
            time.sleep(t)
            t += 0.25
            if t > 7:
                print ' ==> Bad!'
    # 取不到值处理???
    for y in all:
        try:
            top = int(y.get('id').split('_')[-1]) + 1
            url = y.find('a').get('href')
            url = url.strip()
            print top, url
            prices = y.find('span', attrs={
                            'class': 'a-size-base a-color-price s-price a-text-bold'}).get_text()
            items['prices'] = prices
            items['top'] = top
            items['url'] = url
            print top, len(all), prices
            while 1:
                title = get_amazon_item_content(items['url'])
                if title:
                    break
                else:
                    title = get_amazon_item_content(items['url'])
            items['title'] = title
            print top, len(all), prices, title, url
            items['entry_time'] = time.strftime('%Y-%m-%d')
            print items
            amazon_items[top] = url
            all_items.append(items)
        except Exception:
            pass
    return amazon_items


def get_amazon_item_content(url):
    r = check_request(url)
    soup = bs(r.text, 'html.parser')
    title = soup.title.text

    return title

if __name__ == '__main__':
    # from multiprocessing.dummy import Process, Pool
    # from gevent.pool import Group, Pool
    # import gevent

    st = time.time()
    print ' ==> start amazon spider...'
    # p = proxies()
    # all_item = []
    # import grequests
    for x in urls:
        get_amazon_item(x)
    # pool = Pool(4)
    # greenlets = [gevent.spawn(get_amazon_item, x) for x in urls]
    # result = gevent.joinall(greenlets)

    # pool = Pool(processes=4)
    # result = pool.map_async(get_amazon_item, urls).get(1024)

    # result = map(get_amazon_item, urls)

    # for y in all_item:
    #     for x in y.values():
    #         print get_amazon_item_content(x)

    end = time.time()
    print 'spend {0:.2f}'.format((end - st) / 60)
