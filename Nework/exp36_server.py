# ! /usr/bin/python3
# -*- coding: UTF-8 -*-
# 协程实现网络通讯
from threading import current_thread
from gevent import  monkey;monkey.patch_all()#必须打上补丁，如果不用gevent.sleep(1)
from socket import * #补丁一定要在socket模块之前，不然gevent无法识别socket的阻塞
import gevent
def server(ip,port):
    s=socket(AF_INET,SOCK_STREAM)
    s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    s.bind((ip,port))
    s.listen(5)
    print("server %s:%s is running"%(ip,port))
    while True:
        conn,addr=s.accept()
        gevent.spawn(talk,conn,addr)

def talk(conn,addr):
    try:
        print("cilent %s:%s connect" % (addr[0], addr[1]))
        while True:
            res=conn.recv(1024).decode('utf-8')
            print("cilent %s:%s say:%s"%(addr[0],addr[1],res))
            conn.send(res.upper().encode('utf-8'))
            if res=='exit' or not res:
                print("cilent %s:%s break"%(addr[0],addr[1]))
                break
    except Exception as e:
        print(e)
    finally:
        conn.close()
def main():
    server('127.0.0.1',8080)
if __name__ == '__main__':
    main()
    pass