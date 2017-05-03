# coding=utf-8

"""
UDP server
client code in ../client/test_server2.py
"""
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

s.bind(('127.0.0.1', 9999))

# SOCK_DGRAM 指定了这个Socket的类型是UDP
# 绑定端口和TCP一样，但是不需要调用 listen() 方法
# 而是直接接受来自任何客户端的数据

print 'Bind UDP on 9999:'
while True:
    data, addr = s.recvfrom(1024)
    print 'Received from %s:%s' % addr
    s.sendto('hello, %s !' % data, addr)





