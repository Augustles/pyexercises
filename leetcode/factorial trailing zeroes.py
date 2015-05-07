# coding=utf-8

'''
阶乘

'''

def trailingZeroes(n):
    return 0 if n == 0 else n / 5 + trailingZeroes(n / 5)


def factorial(x):
    res = 1
    for i in xrange(2,x+1):
        res *= i
    return res
def fact(x):
    return x > 1 and x * fact(x-1) or 1


f = lambda x:x and x*f(x -1) or 1

print f(5),fact(5),factorial(5)



