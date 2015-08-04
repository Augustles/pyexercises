
lst1 = ['a', 'b', 'c', 'd']
1 如何结束退出一个python脚本
import sys
sys.exit()
2 foo is None 和 foo == None
is相当于id判断,==是value判断
3 如何在循环中获取下标
for index,value in enumerate(lst1):
    print index,value
4 python中如何将一行长代码切成多行
a = 'a' + 'b' + 'c' + 'd' + \
      'e' + 'f' # 在括号中可以直接换行
5 为何 1 in [1,0] == True执行结果是False
(1 in [1,0]) and ([1,0] == True)
6 python中的switch替代语法,  使用词典
def f(x):
    return {'a':1,'b':2}
使用if x is not None:pass
7 在非创建全局变量的地方使用全局变量,global
8 如何检测一个变量是否存在
检测本地变量
if 'myvar' in locals():pass
检测全局变量
if 'myvar' in globals():pass
检测对象是否包含某种属性
if hasattr(lst1,'attr_name'):pass
9 python中是否存在三元运算符
'true' if True  else 'false'
10 python中的do-while
while True:
    stuff()
    if fail_condition:
        break
相对于range(),xrange在python3中丢弃
python中,'i = i + x'和'i += x'什么时候不等
+=调用了__iadd__方法,不存在调用__add__
