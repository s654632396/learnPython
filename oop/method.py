# coding=utf-8

class Person(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def get_grade(self):
        return 'A'


p1 = Person('Bob', 90)
# print p1.get_grade  # <bound method Person.get_grade of <__main__.Person object at 0x7fb9616d9f90>>

import types


class Man(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score


m1 = Man('akarin', 88)


def fn_get_grade(self):
    if self.score > 80:
        return 'A-优秀'
    if self.score >= 60:
        return 'B-及格'
    else:
        return 'C-不及格'


m1.get_grade = types.MethodType(fn_get_grade, m1, Man)

print m1.get_grade()