# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程池聊天软件
import os
from socket import *
from multiprocessing import Pool
# 默认pool进程数是cpu核心数量可用`os.cpu_count()`查询 ps:本机为-12
c = socket(AF_INET, SOCK_STREAM)
c.connect(("127.0.0.1", 8080))


def main():
    while True:
        msg = input(">>:").strip()
        if not msg:
            continue
        c.send(msg.encode('utf-8'))
        msg = c.recv(1024)
        print(msg.decode('utf-8'))


if __name__ == '__main__':
    main()
