#/usr/bin/python
# coding=utf-8

import urllib2

# 读取headers
url = 'http://' + raw_input('please enter your site :')
sock = urllib2.urlopen(url)
i = sock.headers.values()
print i
