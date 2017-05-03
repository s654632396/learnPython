# coding=utf-8

import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?')
print md5.hexdigest() # 32位 16进制 字符串


# 如果数据量大，可以多次update

md5 = hashlib.md5()
md5.update('how to use md5 ')
md5.update('in python hashlib?')
print md5.hexdigest()

sha1 = hashlib.sha1()
sha1.update('how to use md5 in python hashlib?')
print sha1.hexdigest()# 40位 16进制 字符串( 40 * 2^4 bit = 160 bit)