# coding=utf-8

# requests 中文乱码
import requests # 导入requests，需要pip安装
from bs4 import BeautifulSoup # 安装pip install beautifulsoup4
r = requests.get('https://github.com/timeline.json') # 发送一个get请求，相应有post
#print r.text,'/n',r.content,r.encoding,r.status_code() # 响应内容,二进制响应内容,编码,响应状态码
#print r.json(),r.raw() # json响应内容，原始响应内容
#print r.headers
print r.text
soup = BeautifulSoup(r.text)
print soup.title.text
