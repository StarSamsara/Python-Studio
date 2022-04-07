# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# gevent 协程同步和异步
import gevent
import time
from gevent import  monkey;monkey.patch_all()#必须打上补丁，如果不用gevent.sleep(1)

def task(pid):
    time.sleep(0.5)
    print("task %s done"%pid)

def main1():#同步 普通程序
    for i in range(10):
        task(i)
def main2():#异步
    g_l=[gevent.spawn(task,i) for i in range(10)]
    gevent.joinall(g_l)
    print('main done')

if __name__ == '__main__':
    main2()
    pass