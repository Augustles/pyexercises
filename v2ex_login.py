# coding=utf-8

import requests
from bs4 import BeautifulSoup as bs

s = requests.Session()
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:37.0) Gecko/20100101 Firefox/37.0',
    'Origin': 'http://www.v2ex.com',
    'Referer': 'http://www.v2ex.com/signin',
    'Host': 'www.v2ex.com',
    'Accept-Encoding': 'gzip',
    }
r = s.get(r'http://www.v2ex.com/signin', headers=headers)
soup = bs(r.content)
print soup
once = soup.find('input', {'name': 'once'})['value']
login_data = {'u': '***', 'p': '***', 'once': once, 'next': '/'}
s.post('http://www.v2ex.com/signin', login_data, headers=headers)
f = s.get('http://www.v2ex.com/settings', headers=headers)
print f.content
