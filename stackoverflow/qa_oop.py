# coding=utf-8

# oop(面向对象)

# 1.python 'self'解释
# 使用self关键字的原因是，Python没有@语法用于引用实例属性
# 2.为什么python的'private'方法并不是真正的私有方法
# ‘private'只是用作，确保子类不会意外覆写父类的私有方法和属性.不是为了保护外部意外访问而设计的！
# 3.python中类方法的作用是什么
# 当你需要使用不属于任何明确实例的方法,但同时必须涉及类
# 4.python中new和init的用法
# 使用new,但你需要控制一个实例的生成
# 使用init,但你需要控制一个实例的初始化
# new是实例创建的第一步,被优先调用,并且负责返回一个新的实例
# 5.如何获取一个实例的类名
x = len
print x.__name__
# 6.@staticmethod和@classmethod区别
# staticmethod,静态方法在调用时,对类和实例一无所知
# classmethod,在调用时,将会获取到所在的类,或者实例,作为第一个参数
# 7.如何定义静态方法(static method)
class myClass(object):
    @staticmethod
    def the_static_method(x):
        print x
myClass.the_static_method(3)
# 8.python中类变量(环境变量)
class myTest(object):
    """docstring for myTest"""
    i = 2  # i是类级别的变量需和实例的变量i相区别
    def __init__(self, arg):
        super(myTest, self).__init__()
        self.arg = arg
# 9.如何判断一个对象是否拥有某个对象
if hasattr(x,'__name__'):
    print x.__name__
# 10.python有没有简单优雅的方式定义单例类

# 11.理解python中supervision()和init方法

# 12.在python中,如何判断一个对象iterable?
try:
    iterator = iter(x)
except Exception, e:
    print  e
# 13.构造一个基本python迭代器
def counter(low, high):
    current = low
    while current <= high:
        yield current
        current += 1

for c in counter(3, 8):
    print c
# 14.在python中,抽象类和接口有什么区别?
# 在Python中没有（也不需要）一个正式的接口协议
# 15.python中slots
# __slots__的正确使用方法是保存对象的空间
# 限制实例的属性方法
# 16.python,新式类和旧式类的区别
# B是定义的新式类。那么输入b的时候，不论是type(b)，还是b.__class__都是输出的<class '__main__.B'>
# 新式类和旧式类还有一个区别就是再多继承的时候，查找要调用的方法
# 新式类是广度优先的查找算法,旧式类的查找方法是深度优先的
# 17.python中,@property和设置 获取哪一个更好
# 用属性更好，这也是他们存在的原因
# 18.python,链式调用父类构造器

# 19.python,一个对象前面带下划线和双下划线的含义
# 单下划线前缀表示这个属性和方法是私有(保护/私有变量),只有类对象和子类对象自己能访问到这些变量
# 双下划线前缀表示(私有成员),只有类对象自己能访问，连子类对象也不能访问到这个数据
# __xx__双下划线表示定义系统名字
# 20.在一个已存在的对象里,加一个方法

# 21.python,metaclass是什么
# metaclass是class的父类,也可以说是metaclass的实例
# 22.pytyhon的"最小惊奇": 多重默认参数
# python把对象当作一个引用
