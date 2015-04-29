# coding=utf-8
''' 
  1. 比較相鄰的元素。如果第一個比第二個大，就交換他們兩個。
  2. 對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。在這一點，最後的元素應該會是最大的數。
  3. 針對所有的元素重複以上的步驟，除了最後一個。
  4. 持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較
'''
# 冒泡排序算法 * 核心是交换，比较两个大小，大的放前边，小的放后边
def bubbleSort(bubbleList):
    listLength = len(bubbleList)
    while listLength > 0:
        # 循环比较个元素大小
        for i in range(listLength - 1):
            if bubbleList[i] > bubbleList[i+1]: # 切片比较大小
                # 交换值swap
                bubbleList[i] = bubbleList[i] + bubbleList[i+1] 
                bubbleList[i+1] = bubbleList[i] - bubbleList[i+1]
                bubbleList[i] = bubbleList[i] - bubbleList[i+1]
        listLength -= 1
    print bubbleList
 
if __name__ == '__main__':
    bubbleList = range(333)
    bubbleSort(bubbleList)
