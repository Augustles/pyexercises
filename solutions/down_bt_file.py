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


base = 'http://btkitty.so'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.89 Safari/537.36',
    'Referer': base,
    'Accept-Language': 'zh-CN,zh;q=0.8',

}


def downbtkitty(base, keyword):
    p = requests.post(base, headers=headers, data={
                      'keyword': keyword}, timeout=720)

    def get_item(url):
        r = requests.get(url, timeout=720)
        soup = bs(r.text, 'html.parser')
        global d
        d = {}
        all = soup.find('div', attrs={'class': 'list-con'}).find_all('dl')
        for x in all:
            title = x.find('a').get_text().replace('"+"', '')
            title = urllib.unquote(title.encode('utf8'))
            link = x.find('a').get('href')
            d[title] = link
        if not d:
            print(red('=> sorry! not found'))
            sys.exit()

        else:
            for index, x in enumerate(d.iteritems()):
                if os.name == 'nt':
                    print index + 1, x[0].encode('gb2312', 'ignore')
                else:
                    print cyan(index + 1), cyan(x[0])
    print(green('You are in => {0}'.format(p.url)))
    get_item(p.url)

    n = 1

    def input():
        try:
            global i
            if os.name == 'nt':
                i = raw_input('which one to download: ')
            else:
                i = raw_input(green('which one to download: '))
            i = [x for x in i if x != ' ']
        except NameError:
            i = []
    input()

    def down(y):
        x = d.items()[int(y) - 1]
        r = requests.get(x[1], timeout=720)
        print('downloading...{0}'.format(x[0]))
        soup = bs(r.text, 'html.parser')
        for a in soup.find_all('a', attrs={'target': True}):
            if 'Download the' in a.text:
                t = requests.get(a['href'], timeout=720).text
                soup = bs(t, 'html.parser')
                for b in soup.find_all('a', attrs={'target': False}):
                    path = 'http://storebt.com'
                    y = path + b['href']
                    global file
                    file = y.split('/')[-1]
                    rq = requests.get(y, timeout=720)
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
            input()
        elif 'q' in str(i):
            print(red('=> exit'))
            break
        elif 'p' in str(i):
            n = n - 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            print(green('You are in => {0}'.format(url)))
            get_item(url)
            input()
        else:
            n = n + 1
            url = p.url[:p.url.rfind('/0/0') - 1] + \
                str(n) + p.url[p.url.rfind('/0/0'):]
            print(green('You are in => {0}'.format(url)))
            get_item(url)
            input()


if os.name == 'nt':
    # 接受cmd输入时,(gbk),转为utf8编码
    keyword = urllib.quote(
        ''.join(sys.argv[1:]).strip().decode('gb2312').encode('utf8'))
else:
    keyword = urllib.quote(''.join(sys.argv[1:]).strip())
downbtkitty(base, keyword)
