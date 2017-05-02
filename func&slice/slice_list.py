# -*- coding:utf-8 -*-

L = ['akarin', 'haruna', 'kongo', 'yamato', 'shimakaze']

# list的切片处理 [start_index:end_index)
print L[0:3]
print L[1:3]
print L[:3]
print L[3:]
print L[:]
# 切片操作还能指定第三个参数，每隔N个取一个
print L[::2]
print L[::3]
print L[1::2]

r = range(1, 101)
print r
print r[:10]
print r[2::3]
print r[4:50:5]

# 倒序切片
print L[-4::2]
print r[-10:]
print r[-46::5]