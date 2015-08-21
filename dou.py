# coding=utf-8

import requests
from bs4 import BeautifulSoup
import re
import sys
reload(sys)
sys.setdefaultencoding('utf8')

# def get_pic(url):
#     r = requests.get(url)
#     soup = BeautifulSoup(r.text)
#     d = []
#     for pic in soup.find_all('a'):
#         if 'all_photos' in str(pic):
#             r1 = requests.get(pic['href'])
#             soup1 = BeautifulSoup(r1.text)
#             for item in soup1.find_all('a'):
#                 if 'photos/photo' in str(item) and 'albumicon' in str(item):
#                     if 'albumicon' in str(item.img['src']):
#                         if str(item.img['src']) not in d:
#                             d.append(str(item.img['src']).replace('albumicon','photo'))
#     d = list(set(d)) # 去除重复的项
#     for pic in d:
#         file = pic[pic.rindex('/p')+1:]
#         r = requests.get(pic)
#         with open(file,'wb') as w:
#             w.write(r.content)
#     print('download jpg done')






l = 'http://movie.douban.com/subject/26367601/photos?type=S&start=40&sortby=vote&size=a&subtype=a'
l2 = 'http://movie.douban.com/subject/26367601/photos?type=S&start=80&sortby=vote&size=a&subtype=a'
from bs4 import BeautifulSoup as bs
def all_pic(l2):
    r = requests.get(l2)
    s = bs(r.text)
    for n in s.find_all('span',attrs={'class':'count'}):
        m = re.findall(r'\d+',n.text)
        length = round(int(m[0])/40.0+1)
        print length
    e = int(40 * length)
    subjects = []
    f = range(0,e,40)
    for n in f:
        num = 'start='+ str(n)
        url = re.sub(r'start\=\d+', num, l2)
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        n = 0
        for joke in soup.find_all('div', attrs={'class':'cover'}):
            n = n + 1
            thumb =  joke.a.img['src']
            photo = thumb.replace('/thumb','/photo')
            # subjects.append(photo)
            # print photo
            file = photo[photo.rindex('/p')+1:]
            r = requests.get(photo)
            print r.status_code
            with open(file,'wb') as w:
                w.write(r.content)
            
    # for photo in subjects:
    #     file = photo[photo.rindex('/p')+1:]
    #     r = requests.get(photo)
    #     print r.status_code
    #     with open(file,'wb') as w:
    #         w.write(r.content)

all_pic(l2)


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
