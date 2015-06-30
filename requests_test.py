# coding=utf-8

# 保存写入时候出现UnicodeEncodeError:ascii
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

# requests 中文乱码
print(u'\u6c34\u8349\u739b\u7459')
import requests # 导入requests，需要pip安装
from bs4 import BeautifulSoup # 安装pip install beautifulsoup4
r = requests.get('https://github.com/timeline.json') # 发送一个get请求，相应有post
#print r.text,'/n',r.content,r.encoding,r.status_code() # 响应内容,二进制响应内容,编码,响应状态码
#print r.json(),r.raw() # json响应内容，原始响应内容
#print r.headers
print r.text
soup = BeautifulSoup(r.text)
# print soup.title.text



m = requests.get('http://mnwg.net')
s = BeautifulSoup(m.text)
title = s.title.contents # string
keywords = s.select('meta[name="keywords"]') 
description = s.select('meta[name="description"]')
print(title,description,keywords)

for meta in s.find_all('meta'):
    print(meta.get('name'))

# 写入test.html
# with open('test.html', 'a+') as f:
#     for line in m.text:
#         f.write(line)
