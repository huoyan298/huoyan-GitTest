# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
def f1(a,b,c=0,*args,**kw):
    print('a=',a,'b=',b,'c=',c,'args=',args,'kw=',kw)

def f2(a,b,c=0,*,d,**kw):
    print('a=',a,'b=',b,'c=',c,'d=',d,'d=',d,'kw=',kw)


if __name__ =="__main__":

  f1(1,2)

 # f1(1,2,3,'a','b')
 # # 元组和字典都一样
 # f1(2,3,4,'a','c',m=100,x=8,u=78,y=5)
 # # f2的d 参数 我直接使用*args
 # f2(1,2,d=89,ext=None)