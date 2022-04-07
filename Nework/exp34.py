# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# gevent 协程池
import gevent
import time
from threading import current_thread
from gevent import  monkey;monkey.patch_all()#必须打上补丁，如果不用gevent.sleep(1)
def eat(name):
    print("%s eat 1" % name)
    gevent.sleep(2)#模拟拥塞
    print("%s eat 2" % name)
def play(name):
    print("%s play 1" % name)
    gevent.sleep(1)
    print("%s play 2" % name)
def main():
    g1=gevent.spawn(eat,"ming")#创建协程对象
    g2=gevent.spawn(play,"hong")#创建协程对象
    g1.join()
    g2.join()
    print("main")
    pass

def eat1(name):
    print(current_thread().getName())
    print("%s eat 1" % name)
    time.sleep(2)#模拟拥塞
    print(current_thread().getName())
    print("%s eat 2" % name)
def play1(name):
    print(current_thread().getName())
    print("%s play 1" % name)
    time.sleep(1)
    print(current_thread().getName())
    print("%s play 2" % name)
def main1():
    g1=gevent.spawn(eat1,"ming")#创建协程对象
    g2=gevent.spawn(play1,"hong")#创建协程对象
    gevent.joinall([g1,g2])
    print("main")
    pass

if __name__ == '__main__':
    #main()
    main1()
    pass