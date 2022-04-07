# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程锁
import time
import os
import random
from multiprocessing import Process, Manager, Lock


def work(d, lock):
    with lock:
        d['count'] -= 1


def main():
    lock = Lock()  # 初始化进程锁
    with Manager() as m:
        dic = m.dict({'count': 100})
        p_l = []
        for i in range(98):
            p = Process(target=work, args=((dic, lock,)))
            p_l.append(p)
            p.start()
        for p in p_l:
            p.join()
        print(dic)


if __name__ == '__main__':
    main()
