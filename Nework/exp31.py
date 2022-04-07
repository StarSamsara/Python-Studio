# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 迭代锁
from threading import Thread
from threading import RLock as Lock

noodle_lock = fork_lock = Lock()

# RLock内部维护了一个Lock和一个count的变量（记录acquire次数，所以不会死锁）
# 知道一个线程被多次acquire后被release，其他线程才能获得资源
def dkl():  # 死锁进程
    l = Lock()
    l.acquire()
    l.acquire()  # 上面已经拿过一次key了，没有key可拿，阻塞
    print('haha')
    l.release()
    l.release()


def eat1(name):
    noodle_lock.acquire()
    print("%s抢到了面条" % name)
    fork_lock.acquire()
    print("%s抢到了叉子" % name)
    print("%s吃面" % name)
    fork_lock.release()
    noodle_lock.release()


def eat2(name):
    fork_lock.acquire()
    print("%s抢到了叉子" % name)
    noodle_lock.acquire()
    print("%s抢到了面条" % name)
    print("%s吃面" % name)
    noodle_lock.release()
    fork_lock.release()


def main():
    for name in ['顾客1', '顾客2', '顾客3']:
        t1 = Thread(target=eat1, args=(name,))
        t2 = Thread(target=eat2, args=(name,))
        t1.start()
        t2.start()
    pass


if __name__ == '__main__':
    # main()
    # dkl()
    pass
