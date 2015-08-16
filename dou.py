# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re

def down(l):
	global urls
	urls = []
	f = range(0,1000,40)
	for n in f:
		num = 'start='+ str(n)
        url = re.sub(r'start\=\d+', num, l)
        print(url)

def get_pic(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text)
    d = []
    for pic in soup.find_all('a'):
        if 'all_photos' in str(pic):
            r1 = requests.get(pic['href'])
            soup1 = BeautifulSoup(r1.text)
            for item in soup1.find_all('a'):
                if 'photos/photo' in str(item) and 'albumicon' in str(item):
                    if 'albumicon' in str(item.img['src']):
                        if str(item.img['src']) not in d:
                            d.append(str(item.img['src']).replace('albumicon','photo'))
    d = list(set(d)) # 去除重复的项
    for pic in d:
        file = pic[pic.rindex('/p')+1:]
        r = requests.get(pic)
        with open(file,'wb') as w:
            w.write(r.content)
    print('download jpg done')






l = 'http://movie.douban.com/subject/26367601/photos?type=S&start=40&sortby=vote&size=a&subtype=a'
down(l)


if __name__ == '__main__':
    try:
        # 作用于线程
        # pool = multiprocessing.Pool(processes=10)
        # # links为一个序列
        # result = pool.map_async(get_sumary, links).get(240)

        # 作用于进程,需import dummy否则提示没有dummy
        from multiprocessing import dummy,Pool
        pool = Pool(processes=10)
        result = pool.map_async(get_pic, urls).get(240)
    except Exception,e:
        print e
