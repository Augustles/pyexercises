# coding=utf-8
'''
首先在未排序序列中找到最小（大）元素，
存放到排序序列的起始位置，然后，
再从剩余未排序元素中继续寻找最小（大）元素，
然后放到已排序序列的末尾。
以此类推，直到所有元素均排序完毕。
'''
# 选择排序 * 选择最大或者最小置于起始或者末尾
def selectionSort(list):
    list_length = len(list)
    for x in range(list_length):
        min = x
        for y in range(x+1,list_length):
            if list[min] > list[y]:
                min = y
        if min != x:
            list[x],list[min]=list[min],list[x]
    return list

if __name__ == '__main__':
    list2 = range(1000)
    print selectionSort(list2)
