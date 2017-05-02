# -*- coding:utf-8 -*-

d = {
    'akarin' : 14,
    'haruna' : 19,
    'kongo' : 20,
}
print d.values()

# 迭代 dist 中的 value
for v in d.values() :
    print v

# dict除了values()方法，还有一个 itervalues()方法
for v in d.itervalues() :
    print v

# values() 和 itervalues()的不同之处
# values()方法是吧一个dict转成了包含value的新list
# itervalues()则是不会转化，而是在迭代过程中，依次从dict中取出了value
# 节省了生成list所需要的内存
# ==> 类似与 php中的迭代器 和 generator (yield 关键字)

# print d.itervalues()    # <dictionary-valueiterator object at 0x7f96f31b58e8>
# python 中，任何可以迭代的对象都可以用for循环去操作，而内部的迭代是不需要我们关心的

# 如果一个对象说自己可以迭代，那就直接用for去迭代它
# 可见，迭代是一种抽象的数据操作，他不对迭代对象内部的数据有任何要求

d = {
    'akarin' : 14,
    'haruna' : 19,
    'kongo' : 20,
    'yamato' : 21,
    'kaga' : 22,
}

sum = 0.0
for age in d.itervalues():
    sum += age
print sum / len(d)

# 同时迭代 dist 中的key 和value
print d.items() # list中包含 tuple的结构 0 -- key 1-- value
for name, age in d.iteritems():
    print name , ':' , age















