# coding=utf-8

import itertools, time

# naturals = itertools.count(1)
# for n in naturals:
#     print n

# cs = itertools.cycle('abcdefg')
# for c in cs:
#     print c
#     time.sleep(1)

# ns = itertools.repeat('abc', 10)
# for n in ns:
#     print n

# naturals = itertools.count(1)
# ns = itertools.takewhile(lambda x: x <= 20, naturals)
# for n in ns:
#     print n

"""
chain()可以吧一组迭代对象串联起来，形成一个更大的迭代器
"""
l1 = [1, 21, 45, 17, 155]
l2 = ['a', 'cs', 'bs', 'ds']
for ele in itertools.chain(l1, l2):
    print ele

"""
groupby()把迭代器中 相邻 的重复元素跳出来放在一起：
"""

for key, group in itertools.groupby('AAABBBCCCABBBCAA'):
    print key, list(group)

print '\n'
for key, group in itertools.groupby('AAaBbbbBCcCAbbBCaa', lambda x: x.lower()):
    print key, list(group)

print '\n'
"""
imap() 和map()的区别在， imap()可以作用于无穷序列，而且，两个序列长度不一致，会以短的那个为准
imap() 返回的是一个迭代对象
map() 返回的是已经计算好的list
"""
for x in itertools.imap(lambda x, y: x * y, [10, 20, 30], itertools.count(1)):
    print x

"""
ifilter()
"""
print filter(lambda x: x< 5, [1, 3, 5 ,7, 9])
for i in itertools.ifilter(lambda x: x < 5, [1, 3, 5 ,7, 9]):
    print i

















