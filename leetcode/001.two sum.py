# coding=utf-8

'''
一个数组中两个位置上的数的和恰为 target，求这两个位置。 
'''

def twoSum(num, target):
    map = {}
    for i in range(len(num)):
        if num[i] not in map:
            map[target - num[i]] = i + 1
        else:
            return map[num[i]], i + 1
    return -1, -1

print twoSum([1,2,5,5],10)
