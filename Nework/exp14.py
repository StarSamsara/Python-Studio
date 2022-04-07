#! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 支持复杂命令的端口扫描

import socket
from optparse import OptionParser


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
    usage = "usage:xxx.py -i <ip address> -p <port>"
    parser = OptionParser(usage=usage)  # 添加usage方法，xxx.py -h 就会出现以上帮助
    parser.add_option('-i', '--ipaddress', type='string',
                      dest='ipadd', help='your ip address here')
    parser.add_option('-p', '--port', type='string',
                      dest='port', help='your port here')
    (options, args) = parser.parse_args()  # 获取选项和参数进行赋值，并打印
    ip = options.ipadd
    port = options.port
    defaultport = [135, 139, 445, 1433, 3306, 3389, 5944]
    if ',' in port:
        port = port.split(',')
        a = []
        for x in port:
            a.append(int(x))
        scan(ip, a)
    elif '-' in port:
        port = port.split('-')
        s = int(port[0])
        e = int(port[1])
        rscan(ip, s, e)
    elif 'all' in port:
        rscan(ip, 1, 65535)
    elif 'default' in port:
        scan(ip, defaultport)


if __name__ == '__main__':
    main()
