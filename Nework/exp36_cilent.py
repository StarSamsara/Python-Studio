# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 协程实现网络通讯
from socket import *

def main():
    c=socket(AF_INET,SOCK_STREAM)
    c.connect(('127.0.0.1',8080))
    print("connect start")
    while True:
        msg=input(">>:").strip()
        if not msg:continue
        c.send(msg.encode('utf-8'))
        msg=c.recv(1024).decode('utf-8')
        print(msg)
        if msg=='EXIT':
            break
    print("connect over")
if __name__ == '__main__':
    main()
    pass