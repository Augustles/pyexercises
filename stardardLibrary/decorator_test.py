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

def benchmark(func):
    '''
    装饰器打印一个函数的执行时间
    '''
    import time
    def wrapper(*args,**kw):
        t = time.clock()
        res = func(*args,**kw)
        print func.__name__, time.clock() - t
        return res
    return wrapper

def logging(func):
    '''
    装饰器记录函数日志
    '''
    def wrapper(*args,**kw):
        res = func(*args,**kw)
        print func.__name__,args,kw
        return res
    return wrapper

def counter(func):
    '''
    记录并打印一个函数的执行次数
    '''
    def wrapper(*args,**kw):
        res = func(*args,**kw)
        print '{0} has been used: {1}x'.format(func.__name__,wrapper.count)
        return res
    return wrapper

def now_human(func):
    '''
    记录时间
    '''
    import datetime
    def wrapper(*args,**kw):
        res = func(*args,**kw)
        now = datetime.datetime.now()
        print '现在是北京时间{0}:{1}:{2},{3}/{4}/{5}'.format(now.hour,now.minute,now.second,now.day,now.month,now.year)  # .format()格式化字符串
        return res
    return wrapper

@benchmark
@logging
@now_human
def add(x,y):
    return x + y

if __name__ == '__main__':
    print now(),'\n',dir(log),'\n',dir(now) # 调用函数now,log装饰器和普通函数属性没有区别
    print add(3,6)
