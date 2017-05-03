# coding=utf-8

import os

f = open('test', 'r')
print f.tell()
# f.read()
f.read(3)
print f.tell()
f.seek(0, os.SEEK_SET)
print f.tell()
f.read(3)
print f.tell()
f.seek(0, os.SEEK_END)
print f.tell()
f.seek(-5,os.SEEK_CUR)
print f.tell()
print f.read()
f.seek(0, os.SEEK_END)
print f.seek(-17, os.SEEK_CUR)