# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 同步锁
from threading import current_thread, Thread, Lock
import time
n = 50


def work(lock):
    global n
    print("current_thread:", current_thread().getName())
    lock.acquire()
    temp = n
    time.sleep(0.1)
    n = temp-1
    lock.release()


def main():
    lock = Lock()
    l = []
    start = time.time()
    for i in range(n):
        p = Thread(target=work, args=(lock,))
        l.append(p)
        p.start()
    for p in l:
        p.join()
    print('res:', n)
    stop = time.time()-start
    print("main time:", stop)
    pass


if __name__ == '__main__':
    main()
