#!/usr/bin/python

from datetime import datetime

now = datetime.now()
day = str(int(now.day) - 1)
file = r"C:\\mongo\\source\\Report_%s_%s_%s.xls" % (now.month, day, now.year)
print file
#now = datetime.now()
# print "%s:%s:%s,%s/%s/%s" %
# (now.hour,now.minute,now.second,now.day,now.month,now.year)

# with open(r"C:\\mongo\\source\\report.xls","wb") as pf:
#  pass
