# coding=utf-8

from itertools import *
# count,cycle,repeat,takewhile,dropwhile,chain,groupby
# combinations,compress,imap,iflter,islice,izip,permutations
# product,startmap,tee

# 无限迭代器count,cycle
natual = count(1)
# for x in natual:print x # 打印1到无限自然数
cs = cycle('abc')  # 迭代器cs,重复循环序列'abc'
# for c in cs:print c
ns = repeat('a', 5)  # 负责把一个元素重复下去,5为限制个数
for x in ns:
    print x,
# 保留头部元素
ns1 = takewhile(lambda x: x <= 10, natual)
print list(ns1,)  # takewhile作为条件判断
# 跳过头部元素
it = dropwhile(lambda i: i < 4, [2, 1, 4, 1, 3])
print list(it,)
it = chain('abc', 'xyz')  # 把迭代对象串联起来
print list(it)
it = combinations('abcd', 2)
print list(it)

for key, group in groupby('AAABBBCCAAA'):
    print(key, list(group))
