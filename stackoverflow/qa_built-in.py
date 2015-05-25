# coding=utf-8

# built-in内置函数

lst = ['1']
# 1.如何flush python的输出
# 2.默认print输出到sys.stdout
import sys
sys.stdout.flush()
# 3.python如何检测一个对象是list或者tuple,但是不是一个字符串
assert not isinstance(lst, basestring)
# 4.python检查类型权威方法
print lst is str
isinstance(lst,str)
print isinstance(lst,list)
# 5.如何判读一个变量的类型
type(lst)
# 6.python中如何注释一段代码/为什么没有多行zhus
# 7.python中单引号和双引号
# 解析一下python中的闭包
# 对象是数据和方法关联,闭包是函数和数据关联
# 环境变量和一个函数构成一个闭包
# python Lambda why

# 9.python中str和repr的区别
# __repr__的目的是清晰
# __str__的目的是可读性
# 容器的__str__使用已包含对象__repr__
