# coding=utf-8

'''
  1. 将序列每相邻两个数字进行归并操作，形成个序列，排序后每个序列包含两个元素 
  2. 将上述序列再次归并，形成个序列，每个序列包含四个元素 
  3. 重复步骤2，直到所有元素排序完毕 
'''
import sys
sys.setrecursionlimit(1000000)
# 并归排序Ο(n log n)*  递归分解数列，再合并数列
def merge_sort(list):  
    if(len(list) <= 1): return list  
    left = merge_sort(list[:len(list)/2])  
    right = merge_sort(list[len(list)/2:len(list)])  
    result = []  
    while len(left) > 0 and len(right)> 0:  
        if( left[0] > right[0]):  
            result.append(right.pop(0))  
        else:  
            result.append(left.pop(0))  
  
    if(len(left)>0): result.extend(merge_sort(left))  
    else: result.extend(merge_sort(right))  
    return result

'''
def merge_sort(List):  
    mid=int(len(List)/2)  
    if len(List)<=1:return List  
    return merge(merge_sort(List[:mid]),merge_sort(List[mid:]))  
  
def merge(l1,l2):  
    final=[]  
    l1 = sorted(l1)  
    l2 = sorted(l2)  
    while l1 and l2:  
        if l1[0]<=l2[0]:  
            final.append(l1.pop(0))  
        else:  
            final.append(l2.pop(0))  
    return final+l1+l2  
'''

if __name__=="__main__":  
    list2 = range(77777)  
    print merge_sort(list2)  
