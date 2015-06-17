# coding=utf-8

# qa dict stackoverflow 问答

d = {'a':1,'b':2,'c':3}
# 1 使用列表解析创建一个词典
print '1...'
dict2 = dict((key,value) for (key,value) in d.items());print dict2
dict2 = {key:value for (key,value) in d.items()};print dict2
# 使用in还是has_key() in
print '2...'
print u'使用in更pythonic，has_key()在python3删除了'
print 1 in d.values(),'a' in d
# 3 字典默认值
print '3...'

# 4 如何给字典添加一个值
print '4...'
d.update({'d':4});print d
d.update(h=3);print d
dict3 = {'f':5,'g':6}
d.update(dict3);print d
# 5 如何把字段转化一个object，使用对象-属性的方式读取
print '5...'

# 6 如何在单一的表达式中合并两个python词典
print '6...'
z = dict(dict3.items()+ d.items());print z
# 7 如何映射两个列表为一个词典
print '7...'
keys = ['name','age','tel']
values = ['lily',23,1234145]
dict3 = dict(zip(keys,values));print dict3
# 8 排序一个列表所有的dict,根据dict内值
import operator
list2 = sorted(dict3.values(),key=operator.itemgetter('a'));print list2

# 9 根据值排序一个字典
d = {x:y for (x,y) in zip(range(9,1,-2),range(2,7))}
d_key = sorted(d.items(), key=lambda x:[1])
print d_key
# 10 如何将自定义对象作为字典键值
