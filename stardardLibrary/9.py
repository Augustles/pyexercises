# coding=utf-8

# 打印乘法口诀，输出的9.txt
f = open('9.txt', 'a')  # 打开文件,没有则创建，在for循环里可能重复写入丢失之前数据
f.write('9*9乘法口诀' + '\n')  # 写入单行数据read,readline,readlines和write,writelines
for i in range(1, 10):
    for j in range(1, i + 1):
        if i != j:
            data = '%d * %d' % (j, i) + ' = ' + str(i * j) + '\n'
            f.writelines(data)  # 逐行写入
            print data  # 打印
