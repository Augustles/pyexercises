# coding=utf-8

import csv
import pdb

# csv处理
csvfile = open('csv_test.csv', 'wb')  # 写入模式打开
writer = csv.writer(csvfile)  # csv模块写入数据
writer.writerow(['name', 'age', 'tel'])  # 单行写入row
data = [('lily', '23', '123445'), ('tom', '27', '23438'),
        ('sunny', '21', '2348')]  # 多行rows
writer.writerows(data)
csvfile.close()

# 逐行扫描读取
for line in open('csv_test.csv'):
    name, age, tel = line.split(',')
    print name, age, tel

''' # csv模块读取数据
reader = csv.reader(open('csv_test.csv'))
for name, age, tel in reader:
    print name, age, tel
'''
