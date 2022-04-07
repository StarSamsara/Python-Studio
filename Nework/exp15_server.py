#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# UDP通信

import socket


def main():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind(('', 6000))
    while True:
        data, addr = s.recvfrom(1024)
        print('connect by', addr)
        print('recv data:', data.decode('utf-8'))
        s.sendto(data, addr)
    s.close()
    pass


if __name__ == '__main__':
    main()
