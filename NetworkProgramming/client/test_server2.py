# coding=utf-8

"""
server code in ../server/demo2.py
"""

import socket,time

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server = ('127.0.0.1', 9999)

for data in ['haruna', 'kongo', 'Sara', 'Kaga']:
    s.sendto(data, server)
    print s.recv(1024)
    time.sleep(2)

s.close()


