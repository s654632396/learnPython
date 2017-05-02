# coding=utf-8

class Person(object):
    def __init__(self):
        self.attr = 'Person'


class Student(Person):
    # 建议继承父类的写法用这样的形式,而不是用super()
    def __init__(self):
        Person.__init__(self)


class Teacher(Person):
    def __init__(self):
        Person.__init__(self)

class SkillMixin(object):
    pass

class BasketballMixin(SkillMixin):
    def skill(self):
        return 'basketball'

class FootballMixin(SkillMixin):
    def skill(self):
        return 'football'

class BStudent(Student, BasketballMixin):
    def __init__(self):
        Student.__init__(self)

class FTeacher(Teacher, FootballMixin):
    def __init__(self):
        Teacher.__init__(self)

bs = BStudent()
print bs.skill()

ft = FTeacher()
print ft.skill()