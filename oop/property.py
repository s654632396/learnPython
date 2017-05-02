# coding=utf-8

class Student(object):
    __score = 0
    def __init__(self,name, score):
        self.name = name
        self.__score = max(min(score, 100), 0)

    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, score):
        if score > 100 or score < 0 :
            raise ValueError('分数的范围必须在0~100间')
        self.__score = score

s = Student('学生A', 88)
print s.score
s.score = 100
print s.score

