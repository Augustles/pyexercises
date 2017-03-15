#coding=utf-8

# 静态方法,类方法,实例方法
# 单例模式,保证一个类仅有一个实例
# 元类是特殊的类,1.拦截类的创建,2.修改类,3.返回修改后的类
class MyClass(object):
    # __init__是实例方法
    def __init__(self):
        print 'init'
        self._name = 'august'

    @staticmethod  # 静态方法,就是普通函数
    def static_method():
        print 'This is a static method!'

    @classmethod # 把传入self转为cls对象,类方法
    def class_method(cls):
        print 'This is a class method',cls
        print 'visit the property of the class:',cls.name
        print 'visit the static method of the class:',cls.static_method()
        instance = cls()
        print 'visit the normal method  of the class:',instance.test()


    def test(self):
        print 'call test'

    @property # 函数方法转为属性
    def name(self):
        return self._name

class Super_MyClass(MyClass):
    def pprint(self):
        super(Super_MyClass, self).test()

# python类中有三种类方法,实例方法,静态方法(@staticmethod),类方法(@classmethod)
# 实例方法只能被实例方法调用,静态方法或者静态方法可以被类或者实例对象调用
# 实例方法(指类的实例能访问的方法),第一个参数必须要要传实例对象,一般用self
# 静态方法(即普通的函数),参数没有要求
# 类方法(将类本身作为对象进行操作),第一个参数要默认传类,一般用cls

# 可以用super来执行父类的函数

# 1. __new__是一个静态方法,而__init__是一个实例方法
# 2. __new__返回一个实例对象, __init__什么都不返回
# 3. 当__new__返回实例对象时,__init__才会被调用
# 4. 创建新实例调用__new__,初始化一个实例用__init__

# 实现单例方法1, __new__方法
class Singleton(object):
    def __new__(cls, *args, **kw): # __new__静态方法
        if not hasattr(cls, '_instance'):
            # 如果没有实例化_instance, 实例化该类
            orig = super(Singleton, cls)
            cls._instance = orig.__new__(cls, *args, **kw)
        # 否则返回该类
        return cls._instance

# 单例模式2,共享属性
# 所谓的单例模式就是所有的引用(实例,对象)都拥有相同的状态
class Borg(object):
    _state = {}
    def __new__(cls, *args, **kw):
        ob = super(Borg, cls).__new__(cls, *args, **kw)
        # 引用指向(绑定)_state到__dict__
        ob.__dict__ = cls._state
        return ob

class MetaclassTest(type):
    def __new__(cls, *args, **kw):
        if '__str__' not in cls.__dict__:
            raise TypeError('没有定义__str__')
        return super(MetaclassTest, cls).__new__(cls, *args, **kw)

class NNew(Borg):
    # metaclass元类的会拦截类的创建,修改类,返回新的类
    # __metaclass__ = MetaclassTest
    a = 3



if __name__ == '__main__':
    # MyClass.static_method()
    # MyClass.class_method()
    # mc = MyClass()
    # print mc.name
    # ss = Super_MyClass()
    # # MyClass必须继承object否则会报错TypeError
    # ss.test()
    b  = NNew()
    c = NNew()
    print c.a, b.a
    b.a = 333
    print c.a, b.a
    print id(b), id(c)
    # c  = New()
    # print c


