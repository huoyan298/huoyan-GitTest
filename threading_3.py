# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
# import threading
# import time
# counter = 0
# mutex = threading.Lock()

"""
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        global counter
        time.sleep(1)
        counter +=1
        print("I am %s,set counter:%s" %(self.name,counter))

if  __name__ == "__main__":
    for i in range(0,100):
        my_thread =Mythread()
        my_thread.start()
"""
"""
class Mythread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    def run(self):
        global counter,mutex

        if mutex.acquire():
           time.sleep(1)
           counter +=1
           print("I am %s,set counter:%s" %(self.name,counter))
        mutex.release()

if  __name__ == "__main__":
    for i in range(0,100):
        my_thread =Mythread()
        my_thread.start()
"""

from threading import Lock,Thread
from time import sleep,time
lock = Lock()
list1 = [0]*10

def putR(s):
    lock.acquire()
    for i in range(len(list1)):
        list1[i]=1
        print("put ",list1[i])
        sleep(s)
    lock.release()

def getR(s):
    lock.acquire()
    for i in range(len(list1)):
        print("get",list1[i])
        sleep(s)
    lock.release()

if __name__ == "__main__":
    t1 = Thread(target=putR,name ="aa",args =(0.5,))
    t2 = Thread(target=getR,name = "aa",args =(0.5,))

    t2.start()
    t1.start()



    t1.join()
    t2.join()