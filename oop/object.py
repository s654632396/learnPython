# coding=utf-8

class Person(object):
    def __init__(self, name, gender):
        self.name = name
        self.gender = gender


class Student(Person):
    def __init__(self, name, gender, score):
        Person.__init__(self, name, gender)
        self.score = score

    def whoami(self):
        return 'I am a student, my name is %s' % (self.name)

# 使用type() 获取变量的类型，返回一个 Type 对象
print type(123) # <type 'int'>
print type(Student) # <type 'type'>
student = Student('akarin', 'female', 88)
print type(student) # <class '__main__.Student'>

# 使用 dir() 获取变量的所有属性
print dir(123)
    # ['__abs__', '__add__', '__and__', '__class__', '__cmp__', '__coerce__',
    # '__delattr__', '__div__', '__divmod__', '__doc__', '__float__', '__floordiv__',
    # '__format__', '__getattribute__', '__getnewargs__', '__hash__', '__hex__',
    # '__index__', '__init__', '__int__', '__invert__', '__long__', '__lshift__',
    #  '__mod__', '__mul__', '__neg__', '__new__', '__nonzero__', '__oct__',
    # '__or__', '__pos__', '__pow__', '__radd__', '__rand__', '__rdiv__',
    # '__rdivmod__', '__reduce__', '__reduce_ex__', '__repr__', '__rfloordiv__',
    #  '__rlshift__', '__rmod__', '__rmul__', '__ror__', '__rpow__', '__rrshift__',
    # '__rshift__', '__rsub__', '__rtruediv__', '__rxor__', '__setattr__', '__sizeof__',
    # '__str__', '__sub__', '__subclasshook__', '__truediv__', '__trunc__',
    #  '__xor__', 'bit_length', 'conjugate', 'denominator', 'imag', 'numerator', 'real']
print dir(student)
    # ['__class__', '__delattr__', '__dict__', '__doc__', '__format__',
    # '__getattribute__', '__hash__', '__init__', '__module__', '__new__',
    # '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__',
    # '__str__', '__subclasshook__', '__weakref__', 'gender', 'name', 'score',
    # 'whoami']
