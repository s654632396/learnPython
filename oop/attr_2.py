# coding=utf-8

# 修改类属性会影响到所有实例访问的类属性
# 如果在实例上修改类属性会怎么样？

class Person(object):
    address = 'China'

    def __init__(self, name):
        self.name = name

p1 = Person('akarin')
p2 = Person('kongo')

print 'Person.address =' + Person.address
p1.address = 'Shanghai'
print 'p1.address = ' + p1.address

print 'Person.address = ' + Person.address
print 'p2.address = ' + p2.address


