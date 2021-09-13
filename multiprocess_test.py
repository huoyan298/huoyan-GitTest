# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from multiprocessing import Process,freeze_support
import os

def f_print(name):
    print('hello',name)

def info(title):
    print(title)
    print('module name:',__name__)
    print('parent process:',os.getppid())
    print('process id:',os.getpid())

def f(name):
    info('function f')
    print('hello',name)



# if __name__ =='__main__':

if __name__ =='__main__':
  '''
  p = Process(target=f_print,args=('huoyan',))
  p.start()
  p.join()
 '''



  #freeze_support()
  #  os.fork()
  info('main thread')
# freeze_support()
  p=Process(target=f,args=('huoyan',))
  p.start()
  p.join()