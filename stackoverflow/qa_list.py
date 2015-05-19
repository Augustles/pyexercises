# coding=utf-8

# stackoverflow python list 问答
import string,random

# 列表
list2 = ['a','b','c','d','db','thanks']
# 1 判断列表为空
print '1..'
if not list2:
    print 'list2 is empty'
else:
    print 'not empty'
# 2 连接字符串
print '2...'
print '-'.join(list2)  # -为分隔符，把list转为str
# 3 合并两个列表
print '3...'
list3 = [312,4] # 不考虑顺序
list1 = list2 + list3;print list1
# list = list2.extend(list3)
import itertools  # 考虑顺序
for item in itertools.chain(list3,list2):
    print item
# 4 扁平化一个二维数组
print '4...'
list1 = [1,2,3],[4,5,6], [7], [8,9]
list3 = [item for x in list1 for item in x]  # 列表解析
merged = list(itertools.chain.from_iterable(list1));print merged
print sum(list1,[])
# 5 获取一个列表的长度
print '5...'
print len(list2)
print list2.__len__()
# 6 python 复制一个列表
print '6...'
new_list = list2[:];print new_list  # 使用切片
new_list1 = list(list2)  # 使用list函数
import copy  # 使用copy模块
new_list2= copy.copy(list2)
# 7 列表append，extend区别
print '7...'
list2.append([1,3]);print list2
list2.extend([3,5]);print list2
# 8 随机从列表取值
print '8...'
random1 = random.choice(list2);print random1
# 9 利用下标删除一个元素
print '9...'
del list2[1]
list2.pop()  # 默认删除最后一个元素
# 10 获取列表最后一个元素
print '10...'
result = list2[-1]
result1= list2.pop()
# 11 将列表切成长度相同的序列
print '11...'
def chunks(l, n):  # n为要切成的序列
    return [l[i:i+n] for i in range(0, len(l), n)]
print chunks(list2,3)
# 12 列表去重 # sorted(list(set(list2))) 报错 unhashable type: 'list'???
print '12...'
list3 = []
for x in list2:
    if x not in list3:
        list3.append(x)
print list3
# 13 遍历一个list删除某些元素???
print '13...'

#ist2 = [x for x in list2 if list2(x)]
#print list2
# 14 获得list下标
print '14...'
print ['a','b','c'].index('c')
# 15 扁平化一个二维数组
print '15...'
lst1 = [[1,2,3],[4,5,6], [7], [8,9]]
lst2 = [x for y in lst1 for x in y]
# 16 列表解析和map
print '16...'

# 17 列表和元祖有什么区别
print '17...'









