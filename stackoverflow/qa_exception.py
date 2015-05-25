# coding=utf-8

# exception异常

# 1.python中声明exception的方法
class myExcp(Exception):
    pass
# 2.如何人为的抛出异常
# raise Exception('I know python!')
# 3.如何一行内处理多个异常
try:
    10/0
except Exception, e:
    print e

try:
    2/0
except (Exception) as e:print e
# 4.python assert最佳实践
# 5.如何打印到stderr
from __future__ import print_function
import sys
def warning(*objs):
    print sys.stderr

