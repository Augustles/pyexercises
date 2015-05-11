# coding=utf-8

'''
阶乘

'''
# 递归函数，可能产生栈溢出，return
def add1(x):
    res = 1
    for i in xrange(2,x+1):
        res += i
    return res
def factorial(x):
    res = 1
    for i in xrange(2,x+1):
        res *= i
    return res

def fact(x):
    return x > 1 and x * fact(x-1) or 1


f = lambda x:x and x*f(x -1) or 1

f1 = lambda x:x and x+f1(x-1) # 累加

print f(99),fact(100),factorial(5),f1(100),add1(1000)



