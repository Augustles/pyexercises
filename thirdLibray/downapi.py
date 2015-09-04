# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')

from bs4 import BeautifulSoup as bs
import requests
import urllib
import os
import sys
from fabric.colors import red, cyan, green


# 判断网址可用
# lists = ['http://btkitty.la', 'http://www.btkitty.com',
#          'http://www.btkitty.me', 'http://www.btkitty.org']

# for a in lists:
#     try:
#         r = requests.get(a).status_code
#         if r == 200:
#             base = a
#             break
#         else:
#             print(red('God! {0} is bad'.format(a)))
#     except Exception:
#         pass

base = 'http://btkitty.la'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    'Referer': base,
    'Accept-Language': 'zh-CN,zh;q=0.8',

}


def downbtkitty(base, keyword):
    p = requests.post(base, headers=headers, data={
                      'keyword': keyword})

    def get_item(url):
        r = requests.get(url)
        soup = bs(r.text, 'html.parser')
        global d
        d = {}
        for a in soup.find_all('a', attrs={'target': True}):
            link = a['href']
            if 'hehe' in link:
                title = a.text
                d[title] = link
        if not d:
            print(red('....sorry! not found...'))
            sys.exit()

        else:
            for index, x in enumerate(d.iteritems()):
                print cyan(index + 1), cyan(x[0])
    print(green('You are in => {0}'.format(p.url)))
    get_item(p.url)

    n = 1
    try:
        i = raw_input(green('which one to download: '))
        i = [x for x in i if x != ' ']
    except NameError:
        i = []

    def down(y):
        x = d.items()[int(y) - 1]
        r = requests.get(x[1])
        print('downloading...{0}'.format(x[0]))
        soup = bs(r.text, 'html.parser')
        for a in soup.find_all('a', attrs={'target': True}):
            if 'Download the' in a.text:
                t = requests.get(a['href']).text
                soup = bs(t, 'html.parser')
                for b in soup.find_all('a', attrs={'target': False}):
                    path = 'http://storebt.com'
                    y = path + b['href']
                    global file
                    file = y.split('/')[-1]
                    rq = requests.get(y)
                    with open(file, 'wb') as wb:
                        wb.write(rq.content)

    while True:
        pre = ' '.join('0123456789').split()
        if set(i) & set(pre):
            for y in i:
                down(y)
                if os.path.exists(file):
                    print(green(
                        '完成<{0}>下载...'.format(urllib.unquote(keyword))))
                else:
                    print(red('下载失败'))
            n = n + 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            get_item(url)
            try:
                i = raw_input(green('which one to download: '))
                i = [x for x in i if x != ' ']
            except ValueError:
                i = []
        elif 'q' in str(i):
            print(red('...exit..'))
            break
        elif 'p' in str(i):
            n = n - 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            print(green('You are in => {0}'.format(url)))
            get_item(url)
            try:
                i = raw_input(green('which one to download: '))
                i = [x for x in i if x != ' ']
            except ValueError:
                i = []
        else:
            n = n + 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            print(green('You are in => {0}'.format(url)))
            get_item(url)
            try:
                i = raw_input(green('which one to download: '))
                i = [x for x in i if x != ' ']
            except ValueError:
                i = []

# keyword = input(u'当前在 {0}=> 查询种子下载 => '.format(base))

keyword = urllib.quote(''.join(sys.argv[1:]).strip())
downbtkitty(base, keyword)
# try:
#     downbtkitty(base, keyword)
# except NameError:
#     print(red('...God! network is bad...'))
