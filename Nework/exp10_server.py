# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 网络编程基础
import socket


def main():
    s = socket.socket()  # 导入socket模块
    host = socket.gethostname()  # 获取自己的ip地址
    port = 12345  # 使用12345端口通讯
    s.bind((host, port))  # 绑定ip地址和端口
    s.listen(5)  # 等待用户连接，最多五人
    print('服务器运行中')
    c, addr = s.accept()  # 建立和客户端的连接 c=对方的套接字 addr=对方的ip地址
    print("对方的IP地址是：", addr)
    c.send('welcome'.encode("utf-8"))  # 通过客户的套接字发送welcome给对方，utf-8编码
    print(c.recv(1024).decode("utf-8"))  # 接受客户信息，最多1024kb
    c.close()
    s.close()


if __name__ == '__main__':
    main()
