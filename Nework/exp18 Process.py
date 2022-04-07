# !/usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程
import time
import os
import multiprocessing


def test1(a):
    print('test1 start', a)
    print('test1的进程:', os.getpid())
    print('test1的父进程id:', os.getppid())
    time.sleep(3)


def test2(a):
    print('test2 start', a)
    print('test2的进程:', os.getpid())
    print('test2的父进程id:', os.getppid())
    time.sleep(3)


def main():
    print('main函数的进程id是:', os.getpid())
    # 创建进程
    t1 = multiprocessing.Process(target=test1, args=('haha',))
    t2 = multiprocessing.Process(target=test2, args=('nihao',))
    # 启动进程
    t1.start()
    t2.start()
    print('dodododondondondododo')


if __name__ == '__main__':
    main()
