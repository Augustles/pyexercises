# coding=utf-8

import requests
import urllib
import chardet # 检测字符编码
from bs4 import BeautifulSoup
url = 'http://www.liaoxuefeng.com/'
testData = urllib.urlopen(url).read() # 读取内容
r = requests.get(url) # 中文乱码???
#print chardet.detect(testData) # 检测字符
soup = BeautifulSoup(testData)

title = soup.title.text # 有时提示没有text属性
keywords = soup.select('meta[name="keywords"]') 
description = soup.select('meta[name="description"]')
print url,title,keywords,description,soup.p



