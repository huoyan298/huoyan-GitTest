# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
import  threading

class MyThread(threading.Thread):
    def __init__(self):
       threading.Thread.__init__(self);
       #self.setName("new" + self.name)

    def run(self):
        print("I am %s" %self.name)


def main_thread(thread_run):
    thread_list = {}
    #先创建线程对象
    for i in range(0,thread_run):
        thread_name = "thread_%s" %i
        thread_list[thread_name]=MyThread()
        print(thread_list[thread_name])
        thread_list[thread_name].start()

if  __name__ == "__main__":
    # thread_2 = MyThread()
    # thread_2.start()

     main_thread(4)

    # for i in range(0,5):
    #     my_thread =MyThread()
    #     my_thread.start()

