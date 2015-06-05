# coding=utf-8

# time(时间)

# https://blog.linuxeye.com/374.html
# 1.如何将一个python time.struct_time对象转化datetime对象
# from time import mktime
# from datetime import datetime

# dt = datetime.fromtimestamp(mktime(struct))
# 2.python中获取当前时间
import datetime
print datetime.datetime.now() # 获取时间日期
print datetime.datetime.now().time() # 获取时间
# 3.python -time.clock() VS time.time() 更精确
# 哪一个更适合于计时?哪个更精确
# 简而言之, time.clock()更精确些, 但是如果涉及cpu外的硬件时间统计(e.g. gpu), 只能使用time.time()
# 4.python和javascript中json的datetime
