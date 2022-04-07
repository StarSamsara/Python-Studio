#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# UDP通信

import socket


def main():
    c = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        text = input('--->')
        c.sendto(text.encode('utf-8'), ('192.168.98.1', 6000))
        if text == 'exit':
            break
        ans = c.recvfrom(1024)
        print(ans[0].decode('utf-8'))
    c.close()
    pass


if __name__ == '__main__':
    main()
