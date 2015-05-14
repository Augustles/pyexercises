# coding=utf-8

''' 
  1. 比較相鄰的元素。如果第一個比第二個大，就交換他們兩個。
  2. 對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。在這一點，最後的元素應該會是最大的數。
  3. 針對所有的元素重複以上的步驟，除了最後一個。
  4. 持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較
'''

# 冒泡排序算法 * 核心是交换，比较两个大小，大的放前边，小的放后边
def bubbleSort(lst):
    l = len(lst)
    while l > 0:
        # 循环比较个元素大小
        for i in range(l - 1):
            if lst[i] > lst[i+1]: # 切片比较大小
                # 交换值swap
                lst[i] = lst[i] + lst[i+1] 
                lst[i+1] = lst[i] - lst[i+1]
                lst[i] = lst[i] - lst[i+1]
        l -= 1
    return lst
 
if __name__ == '__main__':
    lst = range(333)
    print bubbleSort(lst)
