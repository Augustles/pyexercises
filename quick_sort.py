# coding=utf-8

'''
对数组进行随机化。
从数列中取出一个数作为中轴数(pivot)。
将比这个数大的数放到它的右边，小于或等于它的数放到它的左边。
再对左右区间重复第三步，直到各区间只有一个数。
'''
import sys
sys.setrecursionlimit(1000000)  # 可能会报最大递归深度的错误
# 快速排序,时间复杂度Ο(n log n) * 挖坑填数+分治法
def quickSort(list):
    if not list:  # if len(list)<=1:return list
        return []
    return quickSort([x for x in list[1:] if x < list[0]]) + list[0:1] + \
           quickSort([x for x in list[1:] if x > list[0]])


if __name__=="__main__":
    print quickSort(range(7777))
