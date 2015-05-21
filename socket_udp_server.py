#!/usr/bin/env python
# encoding: utf-8

# 服务端
import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(server_addr)

while True:
    print 'waitting for data'
    data, addr = server.recvfrom(BUF_SIZE)
    print 'Connected by', addr, ' Receive Data: ', data
    server.sendto(data, addr)

server.close()
