#/usr/bin/python

import urllib2

url = 'http://' + raw_input('please enter your site :')
sock = urllib2.urlopen(url)
i = sock.headers.values()
print i