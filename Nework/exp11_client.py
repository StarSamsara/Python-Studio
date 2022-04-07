# ! /usr/bin/python3
# -*- coding: UTF-8 -*-

import socket

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_ip = '192.168.98.1'
server_post = 8999
server_add = ((server_ip, server_post))
tcp_socket.connect(server_add)
first_data = tcp_socket.recv(1024)
print(first_data.decode('utf-8'))
while True:
    # 持续发送数据
    send_data = input("send---->")
    tcp_socket.send(send_data.encode('utf-8'))
tcp_socket.close()
