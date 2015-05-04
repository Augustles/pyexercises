# coding=utf-8

# __slots__,@property,

from types import MethodType
class Student(object):  # 创建一个类,继承object
    #__slots__ = ('name','age','set_age')  # 只允许实例绑定name和age属性
    @property  # __getter__方法变成属性
    def score(self):
        return self._score
    @score.setter  # @property创建了@score.setter
    def score(self,value):  # 对接收的参数进行检查
        if not isinstance(value,int):
            raise ValueError('score must be an interger!')
        if value<0 or value>100:
            raise ValueError('socre must be between 0~100')
        self._score = value

def set_age(self,age):
    self.age = age

def set_score(self,score):
    self.score = score
if __name__ == '__main__':
    s = Student()  # 创建一个实例
    s.name = 'august'  # 为实例绑定一个属性
    s.set_age = MethodType(set_age,s,Student)  # 为实例绑定一个方法
    s.set_age(25)  # 调用set_age方法
    Student.set_age = MethodType(set_age,None,Student)  # 为类绑定一个方法
    s2 = Student()
    #Student.set_score = MethodType(set_score,None,Student)  # 会报AttribuError
    s2.score = 72
    print s2.score
