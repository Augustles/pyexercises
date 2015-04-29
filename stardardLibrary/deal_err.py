# coding=utf-8

# try捕捉错误
try:  # try执行出错，跳到except，如果有finally执行
    print 'try..'
    open('txt')
except Exception, e:
    print e

finally:
    pass
