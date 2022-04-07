# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 线程（Thread）[cpu调度最小单位，同一个进程里的各个线程共享数据，调度和切换速度快]
# 进程 [资源调度最小单位，每个进程中至少有一个线程，地址空间相对独立]只能同一时间干同一件事 在执行过程中如果阻塞，如等待输入，这个时候整个进程是挂起
from threading import Thread
from multiprocessing import Process
import time
import os


def work1():
    print("Hello", os.getpid())


def main1():  # 线程与主进程pid相同
    t1 = Thread(target=work1)
    t2 = Thread(target=work1)
    t1.start()
    t2.start()
    p1 = Process(target=work1)
    p2 = Process(target=work1)
    p1.start()
    p2.start()
    print("main thread", os.getpid())


def work2(n):
    print(n)
    n = 0


def work3(n):
    time.sleep(2)
    print(n)


def main2():
    n = 9
    p1 = Process(target=work2,args=(n,))
    p2 = Process(target=work3,args=(n,))
    p1.start()
    p2.start()
    p1.join()
    p2.join()
    n = 9
    t1 = Thread(target=work2,args=(n,))
    t2 = Thread(target=work3,args=(n,))
    t1.start()
    t2.start()


if __name__ == '__main__':
    #main1()
    #main2()
    pass
