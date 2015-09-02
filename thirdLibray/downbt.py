# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import sys
from fabric.colors import *


# 判断网址可用
lists = ['http://btkitty.la', 'http://www.btkitty.com',
         'http://www.btkitty.me', 'http://www.btkitty.org']

for a in lists:
    try:
        r = requests.get(a).status_code
        if r == 200:
            base = a
            break
        else:
            print('sorry {0} is not active'.format(a))
    except Exception:
        pass


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    'Referer': 'http://btkitty.la/',
    'Accept-Language': 'zh-CN,zh;q=0.8',

}


def downbtkitty(base, keyword):
    p = requests.post(base, headers=headers, data={
                      'keyword': keyword})

    def get_item(url):
        r = requests.get(url)
        soup = bs(r.text)
        global d
        d = {}
        for a in soup.find_all('a', attrs={'target': True}):
            link = a['href']
            if 'hehe' in link:
                title = a.text
                d[title] = link
        for index, x in enumerate(d.iteritems()):
            print cyan(index + 1),cyan(x[0])

    get_item(p.url)

    n = 1
    try:
        i = raw_input(green('which one to download: '))
    except NameError:
        i = ''

    def down():
        x = d.items()[int(i) - 1]
        r = requests.get(x[1])
        print('downloading...{0}'.format(x[0]))
        soup = bs(r.text)
        for a in soup.find_all('a', attrs={'target': True}):
            if 'Download the' in a.text:
                t = requests.get(a['href']).text
                soup = bs(t)
                for b in soup.find_all('a', attrs={'target': False}):
                    path = 'http://storebt.com'
                    y = path + b['href']
                    global file
                    file = y.split('/')[-1]
                    rq = requests.get(y)
                    with open(file, 'wb') as wb:
                        wb.write(rq.content)

            break

    while True:
        if str(i) in '0123456789' and i:
            down()
            if os.path.exists(file):
                print(cyan(
                    '完成<{0}>下载...'.format(urllib.unquote(keyword))))
            else:
                print(red('下载失败'))
            break
        elif 'q' in str(i):
            break
        else:
            n = n + 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            get_item(url)
            try:
                i = raw_input(green('which one to download: '))
            except ValueError:
                i = ''

# keyword = input(u'当前在 {0}=> 查询种子下载 => '.format(base))

keyword = urllib.quote(sys.argv[1].strip())

downbtkitty(base, keyword)
