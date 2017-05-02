# coding=utf-8

# python 中，函数其实也是一个对象
f = abs
print f.__name__
print f(-122)


# 在python中，我们可以给类实例变成一个可以调用的对象
# 只要实现了__call__方法

class Person(object):
    __index = ['name', 'gender']

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender

    def __call__(self, *args):
        for index, val in enumerate(args):
            attr = self.__index[index]
            setattr(self, attr, val)
            if index == len(self.__index) - 1 :
                break


p = Person('akarin', 'female')
p('akarin~', '???', '---')
print p.name
print p.gender
