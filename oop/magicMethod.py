# coding=utf-8

# 特殊方法 / 魔术方法

# 用于 print 的 __str__
# 用于 len 的 __len__
# 用于 cmp 的 __cmp__
# ...

# 定义在class 中
# 不需要直接调用

# 有关联性的特殊方法都必须实现,如：
# __getattr__
# __setattr__
# __delattr__

# __str__ & __repr__
# 将一个类的实例变成 str， 需要实现特殊方法 __str__()
class Person(object):
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return "(Object- Person: %s)" % (self.name)

    __repr__ = __str__


p = Person('akarin')
print p


class Student(Person):
    def __init__(self, name, gender, score):
        Person.__init__(self, name)
        self.gender = gender
        self.score = score

    def __str__(self):
        return "<%s: %s,%s,%s>" % ('Student', self.name, self.gender, self.score)

    __repr__ = __str__

    def __cmp__(self, other):
        if self.score > other.score:
            return 1
        elif self.score == other.score:
            return 0
        else:
            return -1


s = Student('kongo', 'female', 94)
print s
print s.__repr__()

# __cmp__ 定义对象的排序

L = [("kongo", "female", 94), ("haruna", "female", 100), ("bismarck", "female", 93), ]
Ls = [Student(x, y, z) for x, y, z in L]
print Ls
Ls = sorted(Ls)
print Ls


# __len__
class Ships(object):
    def __init__(self, *ars):
        self.lists = {}
        for index, name in enumerate(ars):
            self.lists[index] = name

    def __len__(self):
        return len(self.lists)


s = Ships('haruna', 'kongo', 'yamato', 'shimakaze')
print s.lists
print len(s)

class Fib(object) :
    def __init__(self, num):
        a, b, L = 0, 1, []
        for n in range(num) :
            L.append(a)
            a, b = b, a + b
        self.numbers = L

    def __str__(self):
        return str(self.numbers)

    def __len__(self):
        return len(self.numbers)

    __repr__ = __str__

f = Fib(10)
print f
print len(f)


























