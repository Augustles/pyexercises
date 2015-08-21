# coding=utf-8

import sys
reload(sys)
sys.setdefaultencoding('utf8')
import time
from functools import wraps
# 装饰器，就是对函数，方法和类进行一种加工
# decorator，函数log返回一个函数
def log(text):
    def decorator(func): # 三层嵌套的decorator
        def wrapper(*args,**kw):
            print 'call %s %s():' % (text,func.__name__) # 去函数__name__属性
            return func(*args,**kw)
        return wrapper
    return decorator

@log('execute') # 相当于执行now = log('execute')(now),now = log(now)
def now():
    t = time.time()
    return t

def benchmark(func):
    '''
    装饰器打印一个函数的执行时间
    '''
    import time
    @wraps(func)
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
    @wraps(func)
    def wrapper(*args,**kw):
        res = func(*args,**kw)
        print func.__name__,args,kw
        return res
    return wrapper

def counter(func):
    '''
    记录并打印一个函数的执行次数
    '''
    @wraps(func)
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
    @wraps(func)
    def wrapper(*args,**kw):
        res = func(*args,**kw)
        now = datetime.datetime.now()
        print(u'现在是北京时间 <=> {0}:{1}:{2},{3}/{4}/{5}'.format(now.hour,now.minute,now.second,now.day,now.month,now.year))  # .format()格式化字符串
        return res
    return wrapper

@benchmark
@logging
@now_human # add = benchmark(logging(now_human(add))))
def add(x,y):
    return x + y


def hello(func):
    ''' help doc '''
    @wraps(func)
    def wrapper(*args,**kw):
        print 'hello,%s'%func.__name__
        func(*args,**kw)
        print 'goodbye, %s' %func.__name__
    return wrapper

@hello # plus = hello(plus)
def plus(x,y):
    ''' plus doc '''
    return x*y

def fuck(fn):
    print "fuck %s!" % fn.__name__[::-1].upper()

@fuck  ## wfg= fuck(wfg)
def wfg():
    pass

def makebold(fn):
    ''' 加粗字体 '''
    def wrapper():
        return "<b>" + fn() + "</b>"
    return wrapper

def makeitalic(fn):
    ''' 斜体 '''
    def wrapper():
        return "<i>" + fn() + "</i>"
    return wrapper

@makeitalic
@makebold # 相当于 makebold(test123())
def test123():
    return 'hello'

if __name__ == '__main__':
    print now(),'\n',dir(log),'\n',dir(now) # 调用函数now,log装饰器和普通函数属性没有区别
    print add(3,6)
    print add.__name__
    print plus(3,9)
    print plus.__doc__,plus.__name__
    print test123()
