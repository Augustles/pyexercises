# coding=utf-8

'''
    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28
'''
def titleToNumber(s):
    return reduce(lambda x,y:x*26,map(lambda x:ord(x)-ord('A')+1,s))
if __name__ == '__main__':
    print titleToNumber('x')
