# coding=utf-8

# stackoverflow python问答
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
# 取索引
for index,x in enumerate(list2):print index,x
#global list2 #  在函数使用global变成全局变量
print '-'.join(list2)  # -为分隔符，把list转为str

# 随机生成数字大小写的字符串
print ''.join(random.choice(string.ascii_uppercase + string.ascii_lowercase+ string.digits) for x in range(7))
print 'tadfasdfa'[::-1]  # 反序字串节
# 将字符串转化成字典
import ast
print ast.literal_eval("{'a' : 'b', 'c' : 'd'}")  # 字符串内需对于字典内容
# 填充字符串
n = '3'
print n.zfill(5)
print '000007%d' %(int(n))
print '{0:03d}'.format(5)


# 将列表切成长度相同的序列
def chunks(l, n):  # n为要切成的序列
    return [l[i:i+n] for i in range(0, len(l), n)]
print chunks(list2,3)
# 列表去重 # sorted(list(set(list2))) 报错 unhashable type: 'list'???
list3 = []
for x in list2:
    if x not in list3:
        list3.append(x)
print list3

