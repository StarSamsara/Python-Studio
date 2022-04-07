# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
import socket


def main():
    s = socket.socket()
    host = '192.168.98.1'
    port = 12345
    s.connect((host, port))  # 连接服务器
    msg = input("要发送的信息")
    s.send(msg.encode("utf-8"))  # send message
    print(s.recv(1024).decode("utf-8"))  # 接受信息
    s.close()


if __name__ == '__main__':
    main()
