# -*- coding:utf-8 -*-

# 使用codecs模块方法创建指定编码格式文件

# open(fname, mode, encoding, error, buffering)
# encoding 指定了打开文件的编码格式

import codecs

f = codecs.open('test', 'r+', 'utf-8')
print f.encoding
f.write(u'使用codecs模块方法创建指定编码格式文件')
f.close()