# coding=utf-8

# http://www.lintcode.com/
# http://visualgo.net/index.html
# https://leetcode.com/
# http://hackerxu.com/Twd/
# python一切皆对象它们要么是类的实例，要么是元类的实例
# python对象包含三个要素,id标识一个对象,is是用id判断
# type标识对象的类型,value主要是==进行值的判断
# python中的数字,字符串和元祖的不可变主要体现在会新建一个引用
# 字典和列表的可变主要是python改变了其引用
# 1)特殊方法与多范式
# python中特殊方法(special method) __name__,__len__,
# 连接字符串也是调用对象的特殊方法+ __add__(),内置函数
# list元素的引用list[]就是__getitem__()方法,list[]即__setitem__(3,8),__delitem__('a')
# 函数也是一个对象，任何一个有__call__()特殊方法的对象都被当作函数
# 2)上下文管理器(content manager),语法为with ... as ...
# 会自动关闭文件，实际上是with是定义了__enter__()和__exit__()特殊方法
# 3)对象的属性，python对象可能有多个属性(attribute),dir()获取对象所有的属性和方法
# type获取对象的类型，isinstance判断class的类型
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
# python任何递归函数都会存在栈溢出的可能
# ;可以把语句写在同一行,\可以语句为多行,(),[],{}不用\可以写成多行

# python__init__用来对你的对象进行一些初始化，__del__删除一个类的实例调用
# python中属性和方法区别，属性是变量，方法是函数
# python内置类class属性__name__,__bases__,__dict__,__doc__,__module__
# python内置模块module属性__doc__,__name__,__dict__,__file__
# python内置实例instance属性__dict__,__class__
# python内置函数和方法built-in functions and methods __doc__,__name__,__self__,*__module__
# python def定义的函数__doc__,__name__,*__module__,*__dict__
# python 方法method__doc__,__name__,*__module__
# python 生成器generator__iter__,gi_code,gi_frame,gi_running,next,close,send,throw
# 此外，还有代码块code,栈帧frame,追踪traceback
# 使用inspct模块提供一系列函数用于帮助使用自省
# 检查对象类型,ismodule(obj),is{class|function|method|builtin}(obj),isroutine(obj)是否可调用类型
# 获取对象信息,getmembers(obj)dir,getmodule(obj),get{source|sourcelines}(obj)
# getargspec(func)仅用于方法,getcallargs(func),getmro(cls)

# 面向对象的三大特点,数据封装,继承,多态
# 类class是创建实例的模版instance,实例是一个具体对象,每个实例可以拥有独立的属性
# 继承是把父类的功能都拿过来,有了继承,才有多态
# 多重继承,定制类,元类__slots__,@property,@metaclass,@staticmethod

# python内置object对象,__new__创建类的实例,__init__初始化实例
# __delattr__,getattrbute__,setattr__方法,处理属性的访问
# __hash__,__repr__,__str__方法,print obj 会调用obj.__str__(),找不到则调用__repr__
# __str__的目标是对象信息的可读性,__repr__的目标是对象信息的唯一性,用于程序调试,面向解释器


# 提高python性能的一些库,Numba,pypy,Nuitka,cython,Pyston  LLVM
# python内置函数 abs(),divmod,input,open,staticmethod,all,enmumerate,int,ord,str
# any,eval_r,isinstance,pow,sum,basestring,execfile,issubclass,print,super
# bin,file,iter,property,tuple,bool,filter,len,range,type,bytearray,float,list,raw_input,unichr
# chr,frozenset,long,reload,vars,classmethod,getattr,map,repr,xrange,cmp,globals,max,reversed,zip
# compile,hasattr,memoryview,round,__import__,complex,hash,min,set,apply,exec,eval
# delattr,help,next,setattr,buffer,dict,hex,object,slice,coerce,dir,id,oct,sorted,reversed,intern
# ord('a'),#将字符转换成对应的ASCII码,chr(97),#将ASCII码转换成对应的字符

# python解释器全局锁(gil)可以通过好在现在 Python 易经筋（multiprocessing）, 吸星大法（C 语言扩展机制）和独孤九剑（ctypes）

# python 位运算,~非,&交集,>>,<<位移(转化为二进制移动),|并集,^只存在其中一方的

# TCP三次握手,是指建立一个tcp链接时,需要客户端和服务端总共发送三个包
# 未建立连接时Sequence numbe,和Acknowledgement Number都为0
# client端发送连接syn报文,序列号为0,体现在传输层中Sequence number为0
# server端接收后回复ack,此时ack和syn标志位都为1,将确认序号(Acknowledgement Number)设置为客户的ISN加1
# client端再次向server端发送ack报文,syn标志位为0,
# TCP四次挥手,是指tcp的连接拆除需要发送四个包
# server端或者client端发送fin报文,server或者client端ack确认
