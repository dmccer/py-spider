#!/usr/bin/env python
# encoding: utf-8

# 客户端
import sys
import socket

# 设置缓冲区大小
BUF_SIZE = 1024
# IP 和端口构成表示地址
server_addr = ('127.0.0.1', 8888)

# 生成一个 socket 对象
try:
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Creating Socket Failure. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
    sys.exit()

# 要连接的服务器地址
client.connect(server_addr)

# 发送数据到服务端
while True:
    data = raw_input('Please input some string > ')
    if not data:
        print 'input can\'t empty, Please input again...'
        continue

    # 发送数据到服务器
    client.sendall(data)
    # 接收服务端的数据
    data = client.recv(BUF_SIZE)
    print data

client.close()
