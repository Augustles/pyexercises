# coding=utf-8

'''
reverse integer
Example1: x = 123, return 321
Example2: x = -123, return -321
'''

def reverseInt(x):
    if x == 0:
        res = 0
    elif x < 0:
        res = -1*int(str(abs(x))[::-1])
    else:
        res = int(str(abs(x))[::-1])

    return res

if __name__ == '__main__':
    x = -1534236469
    print reverseInt(x)
