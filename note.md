# python笔记

[lintcode](http://www.lintcode.com/)
[visualgo](http://visualgo.net/index.html)
[leetcode](https://leetcode.com/)
[hackerxu](http://hackerxu.com/Twd/)
## 对象
类是一个模板, 描述对象的行为和状态
对象是类一个实例, 有行为状态和行为
方法是行为
实例变量是描述对象独特实例变量
python一切皆对象它们要么是类的实例,要么是元类的实例
python对象包含三个要素,id标识一个对象,is是用id判断
type标识对象的类型,value主要是==进行值的判断
python中的数字,字符串和元祖的不可变主要体现在会新建一个引用计数
字典和列表的可变主要是python改变了其引用

#### 特殊方法与多范式
python中特殊方法(special method) __name__,__len__,
连接字符串也是调用对象的特殊方法+ __add__(),内置函数
list元素的引用list[]就是__getitem__()方法,list[]即__setitem__(3,8),__delitem__('a')
函数也是一个对象,任何一个有__call__()特殊方法的对象都被当作函数
#### 上下文管理器(content manager)
语法为with ... as ...
会自动关闭文件,实际上是with是定义了__enter__()和__exit__()特殊方法
#### 对象的属性
python对象可能有多个属性(attribute),dir()获取对象所有的属性和方法
type获取对象的类型,isinstance判断class的类型
#### 闭包(closure)
是函数式编程的重要的语法结构
函数和对象的根本目的是以某种逻辑方式组织代码,并提高代码的可重复使用性(reusability)
一个函数和环境变量合在一起,就构成了一个闭包(closure)
闭包能有效减少函数定义参数的数目
#### 装饰器(decorator)
就是对一个函数、方法或者类进行加工
#### python 内存管理
id()查看内存地址
python中每个对象都有存在指向该对象的引用总数,即引用计数(reference count)
可以用sys.getrefcount()查看对象的引用计数
对象可以引用对象两个对象可能相互引用,构成引用环(reference count)
引用对象减少,用del关键字删除某个引用
垃圾回收(garbage collection),当python对象越来越多,python会在适当的时候启用垃圾回收

python任何递归函数都会存在栈溢出的可能
;可以把语句写在同一行,\可以语句为多行,(),[],{}不用\可以写成多行

python__init__用来对你的对象进行一些初始化,__del__删除一个类的实例调用
python中属性和方法区别,属性是变量(os.name),方法是函数(os.listdir())
python内置类class属性__name__,__bases__,__dict__,__doc__,__module__
python内置模块module属性__doc__,__name__,__dict__,__file__
python内置实例instance属性__dict__,__class__
python内置函数和方法built-in functions and methods __doc__,__name__,__self__,*__module__
python def定义的函数__doc__,__name__,*__module__,*__dict__
python 方法method__doc__,__name__,*__module__
python 生成器generator__iter__,gi_code,gi_frame,gi_running,next,close,send,throw
此外,还有代码块code,栈帧frame,追踪traceback
####使用inspct模块提供一系列函数用于帮助使用自省
检查对象类型,ismodule(obj),is{class|function|method|builtin}(obj),isroutine(obj)是否可调用类型
获取对象信息,getmembers(obj)dir,getmodule(obj),get{source|sourcelines}(obj)
getargspec(func)仅用于方法,getcallargs(func),getmro(cls)
### python面向对象
面向对象的三大特点,数据封装,继承,多态
类class是创建实例的模版instance,实例是一个具体对象,每个实例可以拥有独立的属性
继承是把父类的功能都拿过来,有了继承,才有多态
多重继承,定制类,元类__slots__,@property,@metaclass,@staticmethod
class通过__init__()方法传递参数
参数self指向实例本身
python中__init__/__del__会调用回显

python内置object对象,__new__创建类的实例,__init__初始化实例
__delattr__,getattrbute__,setattr__方法,处理属性的访问
__hash__,__repr__,__str__方法,print obj 会调用obj.__str__(),找不到则调用__repr__
__str__的目标是对象信息的可读性,__repr__的目标是对象信息的唯一性,用于程序调试,面向解释器

### python内置函数
abs(),divmod,input,open,staticmethod,all,enmumerate,int,ord,str
any,eval,isinstance,pow,sum,basestring,execfile,issubclass,print,super
bin,file,iter,property,tuple,bool,filter,len,range,type,bytearray,float,list,raw_input,unichr
chr,frozenset,long,reload,vars,classmethod,getattr,map,repr,xrange,cmp,globals,max,reversed,zip
compile,hasattr,memoryview,round,__import__,complex,hash,min,set,apply,exec,eval
delattr,help,next,setattr,buffer,dict,hex,object,slice,coerce,dir,id,oct,sorted,reversed,intern

ord('a'),#将字符转换成对应的ASCII码,chr(97),#将ASCII码转换成对应的字符
uiord('a'),将字符串转化unicode字符串,unichr(97),将97
Event Loop 是计算机系统的一种运行机制,是一个程序结构,用于等待和发送消息和事件
cpu=>工厂,进程=>车间,线程=>工人
进程是一个容器,线程是容器中的工作单位
多进程=>多线程=>阻塞(io同步)=>非阻塞(io异步)=>协程=>(分布式进程)
异步,把任务分成两端,先执行一段,转而执行其他任务,等做好准备,回头来执行第二段
协程是比线程更小的执行体,拥有极高的执行效率
分布式进程,进程
Windows下,多线程的效率比多进程要高
进程是资源分配的最小单位,线程是CPU调度的最小单位
多任务的实现,通常设计master-worker,master负责分配任务,worker负责执行任务
进程(process)是程序在计算机上的一次执行活动,多进程(一般指多个任务),开销大,较稳定,子进程相互不影响,在Windows下创建进程开销巨大
线程(thread)是可执行代码的可分配单元,多线程(单个任务分成不同部分),开销小,稳定性差,一个线程出现问题,导致整个程序崩溃
解释器全局锁gil是指每一个interpreter进程,只能同时仅有一个线程来执行, 获得相关的锁, 存取相关的资源
python解释器全局锁(gil)可以通过好在现在 Python 易经筋（multiprocessing）, 吸星大法（C语言扩展机制）和独孤九剑（ctypes）
1. 进程拥有自己独立的堆和栈，既不共享堆，亦不共享栈，进程由操作系统调度。
2. 线程拥有自己独立的栈和共享的堆，共享堆，不共享栈，线程亦由操作系统调度(标准线程是的)。
3. 协程和线程一样共享堆，不共享栈，协程由程序员在协程的代码里显示调度。
gevent并发(协程)框架,重新包装了os,sys,time,subprocess等标准库
并发的核心思想在于,大的任务可以分解成一系列的子任务,后者可以被调度成 同时执行或异步执行,而不是一次一个地或者同步地执行.两个子任务之间的 切换也就是上下文切换.
提高python性能的一些库,Numba,pypy,Nuitka,cython,Pyston  LLVM

计算密集型任务由于主要消耗CPU资源,因此,代码运行效率至关重要,最好用c语言编写,multiprocessing(使用进程)

IO密集型:涉及到网络、磁盘IO的任务都是IO密集型任务,这类任务的特点是CPU消耗很少,任务的大部分时间都在等待IO操作完成,IO密集型任务最合适的语言是开发效率高,multiprocessing.dummy(使用线程)

python 位运算,~非,&交集,>>,<<位移(转化为二进制移动),|并集,^只存在其中一方的
### TCP三次握手
是指建立一个tcp链接时,需要客户端和服务端总共发送三个包
未建立连接时Sequence numbe,和Acknowledgement Number都为0
client端发送连接syn报文,序列号为0,体现在传输层中Sequence number为0
server端接收后回复ack,此时ack和syn标志位都为1,将确认序号(Acknowledgement Number)设置为客户的ISN加1
client端再次向server端发送ack报文,syn标志位为0,
### TCP四次挥手,是指tcp的连接拆除需要发送四个包
server端或者client端发送fin报文,server或者client端ack确认

### linux
1. 系统
硬件信息, 状态信息,
cpu, uptime, top
memory, top
io, dstat
2. 进程, top, supervisord(进程管理)
进程列表 ps -aux
优先级(renice更改进程优先级)
前台/后天Ctral+Z, fg)
kill/killall
3. 文件系统
磁盘信息(chmod权限/chown拥有人)
磁盘使用情况(du -sh */du -sh/fdisk)
boot(unload/ load kernel.old boot)
已打开文件(lsof)
挂载/从挂(mount/unmount)
4. 网络
4.1 路由(ifconfig/route -n)


