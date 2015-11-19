# coding=utf-8


class Student:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def printf(self):
        return '%s, %d' % (self.name, self.age)

one = Student('hello', 23)  # 实例化
print one.printf()  # 调用方法
print(one.name)  # 调用属性
