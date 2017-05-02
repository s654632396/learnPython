# -*- coding:utf-8 -*-

# operate dict data
d = {
    'akarin': 14,
    'haruna': 19,
    'kongo': 20,
}
for key in d:
    print key, ':', d.get(key)

# set
# set的目的，是一组无重复的无序集合
s = set(['S', 'A', 'B', 'C'])
print s

s = set(['S', 'A', 'B', 'C', 'S'])
print s # 发现，这里的set做了自动去重复处理

# 访问set
# set是无序的集合，所以无法通过索引来访问其中的元素
print 'S' in s
print 'D' in s

# set的内部结构和dict很像，set的元素，类似dict的key，不同在于set没有所谓的value
# 所以，set的元素，也必须是不可变的对象

weeks = set(['MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT', 'SUN'])
x = 'SAT'
if x in weeks :
    print 'ok'
else :
    print 'error input!'

sets = set([('akarin', 95), ('haruna',100), ('kongo', 97)])
for ele in sets :
    print ele[0], ':' , ele[1]

sets.add(('shimakaze', 88))
print sets

sets.remove(('akarin', 95))
print sets


















