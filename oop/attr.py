# coding=utf-8

class Person(object):
    address = 'shanghai'
    count = 0

    def __init__(self, name, age):
        # class attribute
        Person.count = Person.count + 1
        # object attribute
        self.name = name
        self.age = age


print Person.address

# python 是动态语言，所以类的属性也是可以动态修改和创建的
Person.address = 'China'
Person.type = 'humans'
p1 = Person('akarin', 15)
print p1.address
print p1.name
print p1.age
print p1.type

print Person.count  # 1

p2 = Person('kongo', 19)
p3 = Person('haruna', 18)

print Person.count # 3
