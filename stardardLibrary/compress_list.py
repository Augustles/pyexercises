# coding=utf-8

# 去重list整理
list2 = [3,1,8,99,11,32,91,111,319,1111,9913,5,222,3,3,3,'a']

print sorted(list(set(list2)))  # 1）集合，直接用set集合去重
##list3 = list(set(list2)) # 1)2
##print list3.sort()  # list本身有sort方法，对list3进行排序，该方法没有返回值，是对list3排序

##list3 = {}.fromkeys(list2).keys()  # 2)字典，利用dict(哈希表)特性，key值唯一，返回list
##list3.sort()
##print list3
##d = {}  # 2)2 也可以自己构造
##for x in list2:
##    d[x] = 1
##list3 = d.keys()
##list3.sort()
##print list3

##list2.sort()  # 3) 排序后去重
##print [x for i,x in enumerate(list2) if not i or x!=list2[i-1]]

# lst3 = []
# [lst3.append(i) for i in lst3 if not i in list2]

##import itertools # 4) itertools,groupby
##list2.sort()
##print [x[0] for x in itertools.groupby(list2)]

##list3 = []  # 5) 遍历
##for x in list2:
##    if x not in list3:
##        list3.append(x)
##list3.sort()
##print list3

##list3 = reduce(lambda x,y: x if y in x else x+[y],[[],]+list2) # 6)reduce函数
##list3.sort()
##print list3
