# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
#多线程类其他方法
from threading import *
import time
def work():
    time.sleep(3)
    print("child name:",current_thread().getName())#获取线程名字
def main():
    t1=Thread(target=work)
    t2=Thread(target=work)
    t1.start()
    t2.start()
    print("main name:",current_thread().getName())#获取主线程名字
    print("enumerate:",enumerate())#查看还有谁在运行
    print("active_count:",active_count())#查看一共有多少进程在运行
    pass
def main1():
    t1 = Thread(target=work)
    t1.start()
    print('t1.is_alive', t1.is_alive())  # 判断线程是否存活
    t1.join()
    print("main name:", current_thread().getName())
    print('t1.is_alive',t1.is_alive()) #判断线程是否存活
def foo():
    print('1')
    time.sleep(1)
    print("end1")
def bar():
    print('2')
    time.sleep(1)
    print("end2")
def main2():#守护线程
    t1=Thread(target=foo)
    t2=Thread(target=bar)
    t1.daemon=True
    t2.daemon=True
    t1.start()
    t2.start()
    print("main")
if __name__ == '__main__':
    #mian1()
    #main2()
    pass