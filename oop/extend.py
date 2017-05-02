# coding=utf-8

class Person(object):

    def __init__(self, name, score):
        self.name = name
        self.score = score

class Man(Person):

    def __init__(self,name, score, age):
        super(Man, self).__init__(name, score)
        self.age = age
        self.sex = 'male'


class Woman(Person):

    def __init__(self, name, score, age):
        super(Woman, self).__init__(name, score)
        self.age = age
        self.sex = 'female'

m1 = Man('Jack', 90, 22)
w1 = Woman('Alice', 88, 21)
print m1.name
print m1.score
print m1.age
print m1.sex

print w1.name
print w1.score
print w1.age
print w1.sex

p1 = Person('ren', 100)
print isinstance(p1, Person)
print isinstance(p1, Man)
print isinstance(p1, Woman)
print isinstance(m1, Person)
print isinstance(m1, Man)

print isinstance(m1, object)

