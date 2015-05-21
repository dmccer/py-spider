#!/usr/bin/env python
# encoding: utf-8

# 服务端

import sys
import socket

# 设置缓冲区大小
BUF_SIZE = 1024
# IP 和端口构成表示地址
server_addr = ('127.0.0.1', 8888)

# 生成一个 socket 对象
try:
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
except socket.error, msg:
    print 'Creating Socket Failure. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
    sys.exit()
print 'Socket Created'

# 设置地址复用
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# 绑定地址
try:
    server.bind(server_addr)
except socket.error, msg:
    print 'Binding Failure. Error Code: ' + str(msg[0]) + ' Message: ' + msg[1]
    sys.exit()
print 'Socket Bind'

# 监听，最大监听数为 5
server.listen(5)
print 'Socket listening'

# 接受 TCP 链接，并返回新的套接字和地址，阻塞函数
while True:
    client, addr = server.accept()
    print 'Conneted by', addr

    # 从客户端接收数据
    while True:
        data = client.recv(BUF_SIZE)
        print data
        # 发送数据到客户端
        client.sendall(data)

server.close()
