# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# Process模块
import time
import os
from multiprocessing import Process


def f(name):
    print('hello', name)
    print('子进程')


def test1():
    print('test1 start')
    print('test1', os.getpid())
    print('test1 father', os.getppid())
    time.sleep(5)
    print('test1 stop')


def test2():
    print('test2 start')
    print('test2', os.getpid())
    print('test2 father', os.getppid())
    time.sleep(2)
    print('test2 stop')


def main():
    p_list = []
    for i in range(5):
        p = Process(target=f, args=('xiaoming',))
        print('主进程')
        p_list.append(p)
        p.start()
    print(p_list)
    time.sleep(3)
    print()
    print('main start')
    print('main', os.getpid())
    t1 = Process(target=test1)
    t2 = Process(target=test2)
    t1.start()
    t2.start()
    t2.join()  # 主程序阻塞等待t2结束再进行
    print('main stop')

    pass


if __name__ == '__main__':
    main()
