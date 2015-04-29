# coding=utf-8

import time
# 装饰器，就是对函数，方法和类进行一种加工
# decorator，函数log返回一个函数
def log(text):
    def decorator(func): # 三层嵌套的decorator
        def wrapper(*args,**kw):
            print 'call %s %s():' % (text,func.__name__) # 去函数__name__属性
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute') # 相当于执行now = log(now) now = log('execute')(now)
def now():
    t = time.time()
    return t

if __name__ == '__main__':
    print now(),'\n',dir(log),'\n',dir(now) # 调用函数now,log装饰器和普通函数属性没有区别
