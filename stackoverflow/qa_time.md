
time(时间)

https://blog.linuxeye.com/374.html
1.如何将一个python time.struct_time对象转化datetime对象
from time import mktime
from datetime import datetime

dt = datetime.fromtimestamp(mktime(struct))
2. python中获取当前时间
import datetime
print datetime.datetime.now() # 获取时间日期
print datetime.datetime.now().time() # 获取时间
3. python -time.clock() VS time.time() 更精确
哪一个更适合于计时?哪个更精确
简而言之, time.clock()更精确些, 但是如果涉及cpu外的硬件时间统计(e.g. gpu), 只能使用time.time()
4. python和javascript中json的datetime
import time
now = datetime.datetime.now()
date = datetime.date.today()
t = time.time()
s = time.gmtime(t)
print('{0}/{1}/{2}'.format(date.year,date.month,date.day), type(date))
print('{0}/{1}/{2} {3}:{4}:{5}'.format(now.year,now.month,now.day,now.hour,now.minute,now.second), type(now))
print('{0}/{1}/{2} {3}:{4}:{5}'.format(s.tm_year,s.tm_mon,s.tm_mday,s.tm_hour,s.tm_min,s.tm_sec), type(s))
t_date = datetime.datetime.fromtimestamp(t)
print(t_date, type(t_date))


home_date = datetime.strptime(home_date,r"%Y/%m/%d")
if home_date < datetime(2014,12,15):
    continue
if home_date > datetime.now():
    continue
if datetime.now() > home_date + timedelta(days=60):
    continue

datetime convert to string
datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
string convert to datetime
datetime.datetime.strptime("2014-12-31 18:20:10", "%Y-%m-%d %H:%M:%S")
datetime convert to timetuple
datetime.datetime.now().timetuple()
timetuple convert to datetime
datetime.datetime.fromtimestamp(t)
datetime convert to date
datetime.datetime.now().date()
date convert to datetime
datetime.datetime.combine(date, datetime.time())
datetime convert to timestamp
time.mktime(now.timetuple())
timestamp convert to datetime
datetime.datetime.fromtimestamp(1421077403.0)

