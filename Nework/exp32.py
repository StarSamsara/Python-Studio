# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 队列补充
import time
import os
import queue
#Queue.Queue是进程内非阻塞队列。
#multiprocess.Queue是跨进程通信队列。

def main():
    print('先进先出:') 
    q=queue.Queue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    print(q.get())
    print("先进后出:")
    q=queue.LifoQueue()
    q.put(1)
    q.put(2)
    q.put(3)
    print(q.get())
    print(q.get())
    print(q.get())
    print("优先级队列:")
    q = queue.PriorityQueue()
    #q.put((优先值,值))，优先值越小越优先
    q.put((20,1))
    q.put((10,2))
    q.put((30,3))
    print(q.get())
    print(q.get())
    print(q.get())
if __name__ == '__main__':
    main()
