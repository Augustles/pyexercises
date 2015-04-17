#coding=utf-8

# 调试print,assert,logging,pdb

'''
import logging
logging.basicConfig(level=logging.INFO)

def foo(s):
    n = int(s)
    logging.info('n >>> %d' %n) # logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别
    # print 'n >>> %d' % n # print就是有问题的变量打印,简单直接粗暴有效，出现ZeroDivisionError
    # assert n != 0, 'n is zero!' # assert的意思是断言，表达式n != 0应该是True，否则，后面的代码就会AssertionError

    return 10 / n

def main():
    foo('0')

main()
'''

import pdb


s = '0'
n = int(s)
pdb.set_trace() # 运行到这里暂停进入pdb环境，命令p查看变量，n进入下一步,c继续
try: # try来运行这段代码执行出错，则后续代码不会继续执行,跳到exceptp
    print '10/n'
except ZeroDivisionError, e: # 具体错误
    print e # raise

'''
finally:
    print 'finally...'
'''
