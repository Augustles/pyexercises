# coding=utf-8
'''
建立堆，保持最大堆，堆排序（顶端最大元素与最后一个元素不断的交换）
'''
# 堆算法，Ο(n log n)*
def heap_sort(lst):  
    for start in range((len(lst)-2)/2, -1, -1):  
        siftdown(lst,start,len(lst)-1)  
    for end in range(len(lst)-1, 0, -1):  
        lst[end], lst[0] = lst[0], lst[end]  
        siftdown(lst, 0, end - 1)  
    return lst  
  
def siftdown(lst, start, end):  
    root = start  
    while True:  
        child = 2*root + 1  
        if child > end:break  
        if child+1<=end and lst[child] < lst[child+1]:  
            child += 1  
        if lst[child] > lst[root]:  
            lst[child],lst[root] = lst[root],lst[child]  
            root=child  
        else:  
            break

##from heapq import heappush,heappop  
### headp模块
##def heap_sort(iterable):  
##    h = []  
##    for value in iterable:  
##        heappush(h, value)  
##    return [heappop(h) for i in range(len(h))]  
##  

if __name__ == '__main__':
    list2 = range(333)
    print heap_sort(list2)
