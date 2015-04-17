#coding=utf-8

import socket

# socket客户端
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM) # 创建一个socket，AF_INET指定使用ipv4，SOCK_STREAM指定tcp协议
s.connect(('127.0.0.1', 9999)) # 注意connect函数是tuple
print s.recv(1024) # 打印接收的信息，每次最多接受1k字节
for data in ['August', 'Tom', 'Sarah']:
    s.send(data) # 发送数据
    print s.recv(1024)
s.send('exit')
s.close()
