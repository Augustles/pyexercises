# coding=utf-8

'''
计算出len,在读出数
1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.
'''

def countAndSay(n):
    say = '1'
    for i in xrange(n - 1):
        next = ''
        for item in [list(g) for k, g in itertools.groupby(say)]:
            next += str(len(item)) + str(item[0])
        say = next
    return say

if __name__ == '__main__':
    n = '2342'
    print countAndSay(n)
        
