# -*- coding:utf-8 -*-
# 字符串切片
# 字符串 'xxx' 和 u'xxx' 也可以看成是一种list，每一个元素就是一个字符
# 因此字符串也可以切片操作，只是结果仍是字符串

str = 'ABCDEFGH'
print str[:3]
print str[-3:]
print str[::2]

print str.lower()
print 'abc'.upper()

def uc_first(str):
    if len(str) :
        str = str[0].upper() + str[1:].lower()
        return str

print uc_first('hello')