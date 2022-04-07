# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 共享进程队列
import time
import os
import random
from multiprocessing import Process, JoinableQueue


def customer(q, start_time):
    while True:
        res = q.get()
        if res is None:
            break
        time.sleep(random.randint(1, 3))
        print('%s吃了%s' % (os.getpid(), res))
        q.task_done()  # 因为有while，所以用此方法向q.join发送一次信号，证明一个c被处理完，可以结束


def producer(q, name, start_time):
    for i in range(5):
        time.sleep(random.randint(1, 3))
        res = '%s%s' % (name, i+1)
        q.put(res)
        print('%s生产了%s' % (os.getpid(), res))
    print('%s生产完了，耗时%0.2lfs' % (name, int(time.time()-start_time)))
    q.join()  # 生产完毕，使用此方法进行阻塞，直到队列中所有内容（p1,p2,p3,c1,c2）被处理完


def main():
    q = JoinableQueue()
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
    c1.daemon = True
    c2.daemon = True
    # --
    p_1 = [p1, p2, p3, c1, c2]
    for p in p_1:
        p.start()
    # --
    p1.join()
    p2.join()
    p3.join()

    print('food吃完了,耗时%0.2lfs' % (int(time.time() - start_time)))
    print('game stop.')


'''
主进程等待---p1,p2,p3等待---c1,c2 while True
c1,c2 task_done---p1,p2,p3结束---主进程结束---c1,c2因daemon强制结束
'''

if __name__ == '__main__':
    main()
