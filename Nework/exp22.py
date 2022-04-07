# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程间传递数据
import time
import os
import random
from multiprocessing import Process, Queue


def customer(q, start_time):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (os.getpid(), res))
    pass


def producer(q, name, start_time):
    for i in range(5):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (name, i+1)
        q.put(res)
        print('%s生产了%s' % (os.getpid(), res))
    print('%s生产完了'%name)
    print('耗时%0.2lfs' % (int(time.time()-start_time)))


def main():
    q = Queue()
    print('game start:')
    start_time = time.time()
    # ---
    p1 = Process(target=producer, args=(q, '包子', start_time))
    p2 = Process(target=producer, args=(q, '牛肉', start_time))
    p3 = Process(target=producer, args=(q, '面条', start_time))
    # ---
    c1 = Process(target=customer, args=(q, start_time))
    c2 = Process(target=customer, args=(q, start_time))
    # ---
    p1.start()
    p2.start()
    p3.start()
    c1.start()
    c2.start()
    # ---
    p1.join()
    p2.join()
    p3.join()
    # ---
    q.put(None)
    q.put(None)
    # ---
    c1.join()
    c2.join()
    # ---
    print('food吃完了')
    print('耗时%0.2lfs' % (int(time.time() - start_time)))
    print('game stop.')
    # ---
if __name__ == '__main__':
    main()
