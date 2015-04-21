# coding=utf-8

import socket
import time
import threading


def tcplink(sock, addr):
    print 'Accept new connection from %s:%s...' % addr
    sock.send('Welcome!')
    while True:
        data = sock.recv(1024)
        time.sleep(1)
        if data == 'exit' or not data:
            break
        sock.send('Hello, %s!' % data)
    sock.close()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # 创建基于ipv4和tcp的socket
s.bind(('127.0.0.1', 9999))  # 绑定端口，不小1024
s.listen(5)  # 等待listen方法监听端口，传入值
print 'Waiting for connection...'

while True:
    sock, addr = s.accept()
    t = threading.Thread(target=tcplink, args=(sock, addr))
    t.start()

    print 'Connection from %s:%s closed.' % addr
