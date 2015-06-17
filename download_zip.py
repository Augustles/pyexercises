# coding =utf-8

# 下载zip文件
import urllib
import urllib2
import requests
url = 'http://www.blog.pythonlibrary.org/wp-content/uploads/2012/06/wxDbViewer.zip'
r = requests.get(url)
print 'request with loading'
with open('code1.zip','wb') as code:
    code.write(r.content) # 二进制响应内容写入code中
print 'urllib loading'
urllib.urlretrieve(url,'code.zip') # urllib下载
print 'urllib2 loading'
f = urllib2.urlopen(url)
data = f.read()
with open('code2.zip','wb') as code:
    code.write(data)
