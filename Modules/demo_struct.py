# coding=utf-8

import struct

print struct.pack('>I', 10240099)

print struct.unpack('>IH', '\xf0\xf0\xf0\xf0\x80\x80')
# I : 4 byte unsigned int
# H : 2 byte unsigned int

















