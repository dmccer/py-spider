#!/usr/bin/env python
# encoding: utf-8

# 客户端
import socket

BUF_SIZE = 1024
server_addr = ('127.0.0.1', 8888)
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    data = raw_input('Please input data > ')

    if not data:
        print 'The data cannot empty, Please input again  > '
        continue

    client.sendto(data, server_addr)
    data, addr = client.recvfrom(BUF_SIZE)
    print data

client.close()
