#!/usr/bin/python

from datetime import datetime

now = datetime.now()
print "%s:%s:%s,%s/%s/%s" % (now.hour,now.minute,now.second,now.day,now.month,now.year)

