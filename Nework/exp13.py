# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 支持命令的端口扫描器
import sys
import socket

# 判断端口是否开放


def open_judge(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        return True
    except:
        return False


def scan(ip, portlist):
    for x in portlist:
        if open_judge(ip, x):
            print('%s host %s port open' % (ip, x))
        else:
            print('%s host %s port close' % (ip, x))


def rscan(ip, s, e):
    for x in range(s, e):
        if open_judge(ip, x):
            print('%s host %s port open' % (ip, x))
        else:
            print('%s host %s port close' % (ip, x))


def main():
    defaultport = [135, 139, 445, 1433, 3306, 3389, 5944]
    str = sys.argv[1]
    if len(sys.argv) == 2:
        if str[0] == '-':
            option = sys.argv[1][1:]
            if option == 'version':
                print('version is 1.0')
            elif option == 'help':
                print("example:python xxx.py [ip] [port:80,99,89…… or 80-99]")
            sys.exit()
        scan(sys.argv[1], defaultport)
    elif len(sys.argv) == 3:
        if ',' in sys.argv[2]:  # python xx.py ip 80,89,99
            p = sys.argv[2]
            p = p.split(',')
            a = []
            for x in p:
                a.append(int(x))
            scan(sys.argv[1], a)
        elif '-' in sys.argv[2]:  # python xx.py ip 80-99
            p = sys.argv[2].split('-')
            a = []
            s, e = int(p[0]), int(p[1])
            rscan(sys.argv[1], s, e)


if __name__ == '__main__':
    main()
