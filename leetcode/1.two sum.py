# coding=utf-8

def twoSum(num, target):
    dict1 = {}
    for index,value in enumerate(num):
        if target - value in dict1:
            return dict1[target - value] + 1,index + 1
        dict1[value] = index

print twoSum([1,2,5,5],2)
