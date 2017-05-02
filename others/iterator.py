# -*- coding:utf-8 -*-

# 在python中，给定list/tuple，使用for循环来遍历这个list或tuple，这种遍历我们称之为迭代(iteration)

# 在python中，迭代通过for.. in .. 来完成；
# 很多语言是通过 下标来完成的；
# 因此可以看出，python的for循环抽象程度很高；
# python的for不仅可以用在list和tuple上，还可以用在其他任何可以迭代的对象上；

# python的集合
# 有序集合 ： list tuple str unicode
# 无序集合 ： set
# 无序集合且有key-value对： dict

# 迭代与按下标访问数组的不同点是
# 迭代是动词，而后者是一种具体的迭代实现方式，前者只关心迭代结果，根本不关心迭代内部是如何实现的

L = range(1, 101)
# print L
for n in L:
    if n % 7 == 0:
        print n

# 索引迭代
L = ['akarin', 'haruna', 'kongo', 'yamato', 'shimakaze']

# 使用 enumerate() 函数来拿到索引
for index, name in enumerate(L):
    print index, ":", name

# 实际上，迭代的每一个元素是一个tuple
for t in enumerate(L) :
    print t[0] , ':' , t[1]

# zip() 可以把 2个list 变成一个list
# 根据索引相同的部分的元素，组成一个tuple结构的数据

zL = zip(range(1,len(L) + 1), L)

for rank, name in zL :
    print rank , "-" , name
















