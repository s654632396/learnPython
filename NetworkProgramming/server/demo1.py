# coding=utf-8

import socket, threading, time

"""
client连接端代码见 ../client/test_server1.py
"""


# 创建 基于IPv4 & TCP协议的socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定监听端口
# 0.0.0.0绑定到所有的网络地址
# 127.0.0.1绑定到本机
# port < 1024需要管理员权限
s.bind(('127.0.0.1', 9999))

# 开始监听端口
s.listen(5)  # 传入的参数为指定等待连接的最大数量
print 'Waiting for connection..'


def tcplink(sock, addr):
    print 'Accept new Connection from %s:%s...' % addr
    sock.send('welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('hello, %s!' % data)
    sock.close()
    print 'Connection from %s:%s closed.' % addr

while True:
    # 接受一个新连接
    sock, addr = s.accept()
    # 创建新的 thread 来处理TCP连接
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()
