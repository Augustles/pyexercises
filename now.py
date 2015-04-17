#!/usr/bin/python

from datetime import datetime

# 打印时间
now = datetime.now()
print "%s:%s:%s,%s/%s/%s" % (now.hour,now.minute,now.second,now.day,now.month,now.year)
