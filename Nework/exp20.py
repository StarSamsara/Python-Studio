# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 守护进程
import time
from multiprocessing import Process


def foo():
    print('foo start')
    time.sleep(1)
    print('foo stop')


def bar():
    print('bar start')
    time.sleep(2)
    print('bar stop')


def main():
    print('main stop')
    t1 = Process(target=foo)
    t2 = Process(target=bar)
    t1.daemon = True  # 开始守护进程，在start之前开始！！在父进程代码结束后，守护进程立刻停止运行
    t1.start()
    t2.start()
    time.sleep(0.1)
    print('main stop')

    pass


if __name__ == '__main__':
    main()
