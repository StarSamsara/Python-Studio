# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程池聊天软件
import os
from socket import *
from multiprocessing import Pool
# 默认pool进程数是cpu核心数量可用`os.cpu_count()`查询 ps:本机为-12

s = socket(AF_INET, SOCK_STREAM)
# 当socket被关闭之后，立刻重新使用端口

s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
s.bind(('127.0.0.1', 8080))
s.listen(5)


def talk(conn, addr):
    print("进程%s 用户%s" % (os.getpid(), addr))
    while True:
        try:
            msg = conn.recv(1024)
            if not msg:
                break
            conn.send(msg.upper())
            print("%ssay：%s" % (addr, msg.decode('utf-8')))
        except Exception:
            break


def main():
    p = Pool(4)
    print("server is running")
    while True:
        conn, addr = s.accept()
        p.apply_async(talk, args=((conn, addr,)))
    pass


if __name__ == '__main__':
    main()
