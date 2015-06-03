# coding=utf-8

from collections import *
# namedtuple,deque,defaultdict,OrderedDict

Point = namedtuple('Point', ['x', 'y']) # 一个点的二维坐标
p = Point(1,2)
print p.x,p.y,type(p),type(p.x)

circle = namedtuple('circle', ['x' ,'y' ,'r']) # circle用来表示圆

q = deque(['x','y','z','i','j']) # 双端链表
q.append('t')
q.appendleft('a')
print q

d = defaultdict(lambda:'N/A') # 字典返回默认值
d[2] = 3
print(d[2],d[3])

c = Counter() # 统计字符出现的个数
for x in 'programing':
    c[x] += 1
print c

# & 交集, |并集, v1-v2差集(v1有,v2没有), ^对称差集(不会同时出现在v1和v2)
# ('a',1) in v1 判断是否存在

