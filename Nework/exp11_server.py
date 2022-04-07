# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 循环通讯实验
import socket
# ad_inet使用ipv4  sock_stream使用tcp通讯
tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# 绑定端口
tcp_server_socket.bind(("", 8999))
# 允许许多人(128)连接我
tcp_server_socket.listen(128)
# 循环为多个客户端服务多次
print('server is running')
while True:
    # 等待用户连接,保存用户socket和ip
    new_client_socket, client_addr = tcp_server_socket.accept()
    print("the %s connecting" % (str(client_addr)))
    # 给客户发送信息
    new_client_socket.send("welcome".encode('utf-8'))
    # 循环为客户服务
    while True:
        try:
            recv_data = new_client_socket.recv(1024)
            print(recv_data.decode('utf-8'))
        except:
            print('断开连接')
            break
        # 关闭套接字
    new_client_socket.close()
tcp_server_socket.close()
