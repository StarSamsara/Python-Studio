# !/usr/bin/python3
# -*- coding: UTF-8 -*-
# 多线程端口扫描

import socket
from optparse import OptionParser
from threading import Thread


def open(ip, port):
    s = socket.socket()
    try:
        s.connect((ip, port))
        return True
    except:
        return False


def scan(ip, port):
    if open(ip, port):
        print('%s host %s port open' % (ip, port))
    else:
        print('%s host %s port close' % (ip, port))
        pass


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
        for i in a:
            s = Thread(target=scan, args=(ip, i,))
            s.start()
    elif '-' in port:
        port = port.split('-')
        s = int(port[0])
        e = int(port[1])
        for i in range(s, e):
            s = Thread(target=scan, args=(ip, i,))
            s.start()
    elif 'all' in port:
        for i in range(1, 65545):
            s = Thread(target=scan, args=(ip, i,))
            s.start()
    elif 'default' in port:
        for i in defaultport:
            s = Thread(target=scan, args=(ip, i,))
            s.start()


if __name__ == '__main__':
    main()
