# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程池
import time
import os
from multiprocessing import Pool, Process


def func(n):
    for i in range(10):
        print(n+1)


def cps():
    # 进程池1与多进程2运行效率对比
    start = time.time()
    pool = Pool(5)
    pool.map(func, range(100))
    t1 = (time.time()-start)
    start = time.time()
    p_list = []
    for i in range(100):
        p = Process(target=func, args=(i,))
        p_list.append(p)
        p.start()
    for p in p_list:
        p.join()
    t2 = (time.time()-start)
    print(t1)
    print(t2)


def work(n):
    print("%s is running" % (os.getpid()))
    time.sleep(1)
    return n**2


def tbw():
    p = Pool(3)  # 以后就用这从无到有三个进程执行任务
    res_l = []
    for i in range(10):
        res = p.apply(work, args=(i,))  # 同步调用，直到拿到结果为止，不管任务是否存在阻塞，同步调用都会在原地等待
        res_l.append(res)
    print(res_l)

def ybw():
    p = Pool(3)  # 以后就用这从无到有三个进程执行任务
    res_l = []
    for i in range(10):
        res = p.apply_async(work, args=(i,))  # 异步调用，直三个进程不会同时开启同时结束
        res_l.append(res.get()) #不用get，得到的res不是值，而是一个对象地址
    p.close()
    p.join()#异步提交任务，主进程需要使用join等待进程池里任务都处理完后，可用get搜集结果
    #如果不用join，主进程结束，进程池还没来得及执行，跟着结束。
    print(res_l)

def main():
    ybw()

if __name__ == '__main__':
    main()
