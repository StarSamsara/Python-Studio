# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
import socket
import os

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = '192.168.98.1'
port = 12345
client_socket.connect((host, port))
while True:
    recv = client_socket.recv(1024).decode('utf-8')
    print(recv)
    msg = input('send message:')
    client_socket.send(msg.encode('utf-8'))
client.close()
