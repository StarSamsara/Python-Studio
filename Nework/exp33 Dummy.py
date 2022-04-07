# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 进程[资源调度最小单位]
# 线程[cpu调度最小单位]
# 协程（DummyThread伪线程）[用户态的轻量级线程]单线程遇到io，就会从应用程序级别进行控制和切换
'''
优点：
切换开销跟小，属于程序级别的切换，操作系统感知不到
单线程实现并发效果
缺点：
协程都是基于单线程的
一旦协程出现阻塞，就会阻塞整个线程
'''


import time
from greenlet import greenlet


def create_num(all_num):
    print("---1---")
    a, b = 0, 1
    current_num = 0
    while current_num < all_num:
        print('---2---')
        ret = yield a
        print("---ret---", ret)
        print('---3---')
        a, b = b, a+b
        current_num += 1
        print('---4---')


def main1():
    obj = create_num(10)
    ret = next(obj)
    print(ret)
    ret = obj.send('haha')
    print(ret)
    pass


def task_1():
    while True:
        print('---1---')
        time.sleep(1)
        yield


def task_2():
    while True:
        print('---2---')
        time.sleep(1)
        yield


def main2():
    t1 = task_1()
    t2 = task_2()
    while True:
        next(t1)
        next(t2)


def main3():
    def eat(name):
        print("%s eat 1" % name)
        g2.switch('hong')
        print("%s eat 2" % name)
        g2.switch()

    def play(name):
        print("%s play 1" % name)
        g1.switch()
        print("%s play 2" % name)
    g1 = greenlet(eat)
    g2 = greenlet(play)
    g1.switch('ming')


def f1():
    res = 0
    for i in range(100):
        res += 1
        time.sleep(0.1)
        print(res)


def f2():
    res = 0
    for i in range(100):
        res += 2
        time.sleep(0.1)
        print(res)


g1 = greenlet(f1)
g2 = greenlet(f2)
def main():
    start=time.time()
    g1
    stop=time.time()
if __name__ == '__main__':
    # main1()
    # main2()
    main3()
    pass
