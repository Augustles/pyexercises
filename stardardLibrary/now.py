#!/usr/bin/python

from datetime import datetime, timedelta

import time
print time.strftime('%Y-%m-%d')

now = datetime.now()
day = timedelta(1) + now
file = r"C:\\mongo\\source\\Report-%s-%s-%s.xls" % (day.day, day.month, day.year)
print file
# (now.hour,now.minute,now.second,now.day,now.month,now.year)

