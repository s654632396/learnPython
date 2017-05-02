# coding=utf-8

# python是动态语言，所以可以在运行期间动态添加属性
# 如何限制添加的属性？
# 利用python 的 __slots__

class Student(object):
    __slots__ = ('name', 'gender', 'score')

    def __init__(self, name, gender, score):
        self.name = name
        self.gender = gender
        self.score = score


s = Student('akarin', 'female', 85)


# s.grade = 'A' # AttributeError: 'Student' object has no attribute 'grade'

class Person(object):
    __slots__ = ('name', 'gender')

    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Teacher(Person):
    __slots__ = ('score',)

    def __init__(self, name, gender, score):
        Person.__init__(self, name, gender)
        self.score = score

t = Teacher('laoshi', 'male', 100)
print t.name
print t.gender
print t.score