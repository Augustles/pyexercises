# coding=utf-8
'''
  1. 从第一个元素开始，该元素可以认为已经被排序
  2. 取出下一个元素，在已经排序的元素序列中从后向前扫描
  3. 如果该元素（已排序）大于新元素，将该元素移到下一位置
  4. 重复步骤3，直到找到已排序的元素小于或者等于新元素的位置
  5. 将新元素插入到该位置后
  6. 重复步骤2~5
  最差时间复杂度：O(n^2)
  最优时间复杂度：O(n)
  平均时间复杂度：O(n^2)
'''
# 插入排序 * 取一个数，从后往前扫描插入
def insertSort(list):
    length_list = len(list)
    # 取出list值
    for x in range(1,length_list):
        key = list[x]

        for y in range(1,x+1)[::-1]:
            if y>0 and key < list[y-1]:
                list[y] = list[y-1]
                list[y-1] = key
    return list

if __name__ == '__main__':
    list2 = range(7777)
    print insertSort(list2)
