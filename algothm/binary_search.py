# coding=utf-8

# 查找算法的二分法
def binarySearch(list,value):
    begin = 0
    end = len(list)-1
    if list[0] == value:
        return 0
    while(begin < end):
        mid = begin + (end - begin)//2
        if list[mid]>value:
            end = mid - 1
        elif list[mid] <value:
            begin = mid + 1
        else:
            return 'position %d' %mid

    if(begin == end):
        if(value == list[begin]):
            return begin
        else:
            return -1
        

if __name__ == '__main__':
    list3 = [2,2,1,2,3,4,5,6]# 只能查找第一个值
    print binarySearch(list3,5)
