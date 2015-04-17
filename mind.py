#coding=utf-8

import random

def how_to(a,b=2,*args,**kw): # 一般来说*args为可变常数接收的是tuple，**kw为关键词常数接收为dict
    # b如果没有默认值，前者a不能有默认，否则报SyntaxError
    options = ['design','model','code','debug','refactor','communicate','learn','think']
    minds = ['想的明白','算的准确','写的清楚']
    print random.choice(options),random.choice(minds)
    print args,kw

if __name__ == '__main__':
	how_to(3,5,3,9,x=3) # 函数可以接收任何值

