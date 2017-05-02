# coding=utf-8

class Person(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def get_name(self):
        return self.__name

    def get_grade(self):
        if self.__score >80 :
            return 'A-优秀'
        if self.__score >= 60 :
            return 'B-及格'
        else:
            return 'C-不及格'

p1 = Person('bob', 77)
print p1.get_name()
print p1.get_grade()

