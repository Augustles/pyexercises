# coding=utf-8

import functools

int2_1 = functools.partial(int,base=2)
int8 = functools.partial(int,base=8)

def int2(x,base=2):  # 二进制字符串转化为整型
    return int(x,base)


if __name__ == '__main__':
    print int2('100000')
    print int2_1('1111111')
    print int8('1231234341')
    
