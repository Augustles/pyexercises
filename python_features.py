# encoding=utf-8


def foo(x, y):  # 函数参数unpack
    print x, y
l = [2, 3]
d = {'x': 2, 'y': 3}
print foo(*l), foo(**d)

for index, n in enumerate(range(2, 7), 1):  # 指明索引起始值
    print index, n
