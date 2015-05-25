# coding=utf-8

# 函数

# 1.如何获取一个函数名的字符串
print len.__name__
# 2.用函数名字字符串调用一个函数

# 3.python中*和**的作用
# *把函数所有参数转化为tuple序列,但你不清楚有多少个参数传进来时使用
# **把函数关键字参数转为一个字典
# *可以用于函数调用时参数列表解包(unpack)
# 4.在python中使用**的合适方法

# 5.构造一个基本的python迭代器
# 意味着python提供iter()和next方法
class Counter:
    def __init__(self, low, high):
        self.current = low
        self.high = high

    def __iter__(self):
        return self

    def next(self): # Python 3: def __next__(self)
        if self.current > self.high:
            raise StopIteration
        else:
            self.current += 1
            return self.current - 1


for c in Counter(3, 8):
    print c
# 6.*args和**kwargs是什么
# 同3
# 7.在python中,如何干净,pythonic的实现一个复合构造函数

# 8.为什么在python的函数中,代码运行速度更快
# 存储在本地变量的比全局变量运行速度更快


