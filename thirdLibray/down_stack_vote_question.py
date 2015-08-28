# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import requests
from bs4 import BeautifulSoup
import re
import os


def down_vote(urls, out):
    d = []
    # 清空temp和out
    if os.path.exists('temp.txt'):
        os.remove('temp.txt')
    if os.path.exists(out):
        os.remove(out)
    # 构造url
    for n in range(1, 11):
        num = 'page=' + str(n)
        url = re.sub(r'page\=\d+', num, urls)
        d.append(url)
    # 查找question写入
    for url in d:
        r = requests.get(url)
        soup = BeautifulSoup(r.text)
        for i, h3 in enumerate(soup.find_all('h3')):
            if 'current community' in h3.text or 'your communities' \
                    in h3.text or 'more stack exchange communities' in h3.text:
                pass
            else:
                with open('temp.txt', 'a') as a:
                    a.write(h3.text + '\n')
    # 添加序号
    with open('temp.txt', 'r') as r, open(out, 'a') as a:
        for index, line in enumerate(r):
            new = str(index + 1) + '. ' + line
            print(new)
            a.write(new)

urls = r'http://stackoverflow.com/questions/tagged/python?page=2&sort=votes&pagesize=50'
out = 'python_vote.md'
down_vote(urls, out)
