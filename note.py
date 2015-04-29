# coding=utf-8

# python一切皆对象
# 1)特殊方法与多范式 
# python中特殊方法(special method) __name__,__len__,
# 连接字符串也是调用对象的特殊方法+ __add__(),内置函数
# list元素的引用list[]就是__getitem__()方法,list[]即__setitem__(3,8),__delitem__('a')
# 函数也是一个对象，任何一个有__call__()特殊方法的对象都被当作函数
# 2)上下文管理器(content manager),语法为with ... as ...
# 会自动关闭文件，实际上是with是定义了__enter__()和__exit__()特殊方法
# 3)对象的属性，python对象可能有多个属性(attribute)
# 4)闭包(closure)是函数式编程的重要的语法结构
# 函数和对象的根本目的是以某种逻辑方式组织代码，并提高代码的可重复使用性(reusability)
# 一个函数和环境变量合在一起，就构成了一个闭包(closure)
# 闭包能有效减少函数定义参数的数目
# 5) 装饰器(decorator),就是对一个函数、方法或者类进行加工，
# 6) python 内存管理，id()查看内存地址
# python中每个对象都有存在指向该对象的引用总数，即引用计数(reference count)
# 可以用sys.getrefcount()查看对象的引用计数
# 对象可以引用对象两个对象可能相互引用，构成引用环(reference count)
# 引用对象减少,用del关键字删除某个引用
# 垃圾回收(garbage collection),当python对象越来越多，python会在适当的时候启用垃圾回收


