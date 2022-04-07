# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 队列
import time
import os
from multiprocessing import Process, Queue


def main():
    q = Queue(3)  # 先进先出
    try:
        q.put('h1')
        q.put('h2')
        q.put('h3')
        # q.put('h4') 队列已满，程序在此处阻塞，等待队列中数据被人取走，再将数据放入队列
        q.put_nowait('h4')  # 如果满了不会阻塞但会报错
    except:
        print("full,cannot put")
        print("Is full:", q.full())
    try:
        print(q.get())
        print(q.get())
        print(q.get())
        # print(q.get()) 队列已空，程序在此处阻塞，等待队列中数据放入数据，再将数据取出
        q.get_nowait()
    except:
        print("empty,cannot get")
        print("Is empty:", q.empty())


if __name__ == '__main__':
    main()
