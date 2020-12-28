# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyan
# @Site    : 
# @File    : 
# @Software: PyCharm
import datetime
from decorator import decorate
import logging

import os.path
import time

import xlrd
import xlwt

'''
打开文件 写文件 
装饰器的各种形式
logging 基础用法
xlrd,xlwt base 用法
'''


# import os
# import sys
# import itertools as its
# words=['123','qwe','zxc','0-=','[]\\',',./']
# r1 =its.product(words,repeat=4)
# dic = open("pass1.txt","a")
# for i in r1:
#     i=list(i)
#     temp=""
#     for k in i:
#         temp=temp+k
#     dic.write(temp+'\n')
# r2 =its.product(words,repeat=5)
# for i in r2:
#     i=list(i)
#     temp=""
#     for k in i:
#         temp=temp+k
#     dic.write(temp+'\n')
# r3 =its.product(words,repeat=6)
# for i in r3:
#     i=list(i)
#     temp=""
#     for k in i:
#         temp=temp+k
#     dic.write(temp+'\n')

# 装饰器一  简单的装饰器
# def debug(func):
#     def wrapper():
#         print("[debug]:enter:{}()".format(func.__name__))
#         return func()
#     return  wrapper
#
# def say_hello():
#     print("hello!")
#类似于       say_hello=debug(say_hello)

# 装饰器二 对原函数做了包装，并返回了另外一个函数
# def debug(func):
#     def wrapper():
#         print("[debug]:enter:{}()".format(func.__name__))
#         print("yufatang")
#         return func()
#     return  wrapper
#
# @debug
# def say_hello():
#     print("hello!")

# 装饰器三  被装饰的函数需要传入参数 单一一个参数
# def debug(func):
#     def wapper(something):
#         print("[debug]:enter{}[]".format(func.__name__))
#         return func(something)
#     return  wapper

# def debug(func):
#     def wapper(something):
#         print("[debug]_one:enter{}[]".format(func.__name__))
#         return func(something)
#     return wapper

# @debug
# def say(something):
#     print("hello{}!".format(something))

# 装饰器四  被装饰的函数传入的参数 类型多样
# def debug(func):
#     def wrapper(*args,**kwargs):
#         print("[DEBUG]:enter {}() ".format(func.__name__))
#         print("prepare and say...")
#         return  func(*args,**kwargs)
#     return  wrapper
# #
# @debug
# def say(something):
#     print("hello{}!".format(something))


# 高级一点的装饰器  带参数的装饰器    （被装饰器装饰的函数 带参数）
# def logging(level: object) -> object:
#     print("logging level begin_1")
#     def wrapper(func):
#         print("wrapper func begin_2")
#         def inner_wrapper(*args, **kwargs):
#             print("inner_wrapper begin")
#             print( "[{level}]:enter function {func}()".format( level=level, func=func.__name__ ) )
#             print("func end")
#             return func( *args, **kwargs )
#             print("inner_wrapper end")
#         return inner_wrapper
#         print("inner_wrapper")
#     return wrapper

# def logging(level):
#      def wrapper(func):
#          def inner_wrapper(*args, **kwargs):
#              print( "[{level}]:enter function {func}()".format( level=level, func=func.__name__ ) )
#              return func( *args, **kwargs )
#          return inner_wrapper
#      return wrapper

# 装饰器五（1）
# @logging(level = 'INFO')
# def say(something):
#     print("say{}!".format(something))
#
#
# @logging( level= 'Wranning' )
# def warn(something):
#     print("warn{}!".format(something))
#
# @logging(level='DEBUG')
# def do(something):
#     print("do {}...".format(something))


# 装饰器五（2）没有使用@语法
# def say(something):
#     print("say{}!".format(something))
#
# say = logging(level='INFO')(say)

# 装饰器六 内置方法__call__ 魔法方法
# class Test():
#     def __call__(self):
#         print("call me!")

# 装饰器七 类的构造函数接受一个函数，然后重载__call__()并返回一个函数
# 也可以达到装饰器函数的效果
# class logging(object):
#     def __init__(self,func):
#         self.func =func
#
#     def __call__(self, *args, **kwargs):
#         print("[DEBUG]:enter function{func}()".format(func =self.func.__name__))
#         return self.func(*args,**kwargs)
#
# @logging
# def say(something):
#     print("say {}!".format(something))



# 装饰器八  带参数的类装饰器
# 如果需要通过类形式实现带参数的装饰器
# 构造函数里接受的不是一函数，而是传入的参数
# 通过类把这些参数保存起来，然后重载__call__就是需要接受一个函数并返回一个函数
# class logging(object):
#     def __init__(self,level='INFO'):
#         self.level = level
#
#     def __call__(self,func):#接受函数
#         def wrapper(*args,**kwargs):
#             print("[{level}]:enter function {func})()".format(level =self.level,
#             func =func.__name__))
#             return func(*args,**kwargs)
#         return  wrapper #返回函数
#
# @logging(level ='INFO')
# def say(something):
#     print("say{}!".format(something))


# 装饰器九 内置的装饰器 @property
# def getx(self):
#     return self._x
#
# def setx(self,value):
#     self._x = value
#
# def delx(self):
#     del self._x

# create a property  python属性标准写法，使用@语法
# x = property(getx,setx,delx,"I am doc for x property")

# @property
# def x(self):...
# 等同于
# def x(self):
# x = property(x)

# 属性有三个装饰器：setter,getter,deleter
# 都是在property()的基础上做一些封装，因为setter 和 deleter是
# property()的第二个和第三个参数，不能直接套用@语法，getter装饰器
# 和不带getter的属性装饰器效果是一样的，估计只是为了凑数，本身没任何
# 存在的意义，经过@property装饰过的函数返回的不再是一个函数而是一个
# propert对象 例如

#      @name.setter
#     def name(self, name):
#         if isinstance(name, str):
#             self.__name = name
#         else:
#             raise TypeError("The name must be str")


# 装饰器九
# @staticmethod 返回的是一个 staticmethod 类对象
# @classmethod 返回的是一个 classmethod类对象，
# 它们都是调用的各自的__init__()构造函数

# class classmethod(object):
#     """
#     classmethod(function)-> method
#     """
#     def  __init__(self,function):
#     #for @classmethod decorator
#         pass
#
# class staticmethod(object):
#     """
#     staticmethod(function)->method
#     for @staticmethod decorator
#     """
#    def __init__(self,function)
#        pass

# 装饰器的@语法等同调用了这两个类的构造函数
# class Foo(object):
#     @staticmethod
#     def bar():
#        pass
# 等同于  bar = staticmethod(bar)

# 位置错误的代码  为什么装饰器函数是这样顺序执行的呢
def html_tags(tag_name):
    print("begin outer function")
    def  wrapper_(func):
        print("begin of inner wrapper function")
        def wrapper(*args,**kwargs):
            content = func(*args,**kwargs)
            print("<{tag}> {content} </{tag}>".format(tag=tag_name,content=content))
            print("end of inner wrapper function")
        return wrapper
    print("end of outer function")
    return wrapper_


@html_tags("b")
def html_hello(name="Toby"):
    return ("hello {}!".format(name))


# 错误的函数签名和文档 十
# 装饰器装饰过的函数看上去名字没变，其实已经变了

# def logging(func):
#      def wrapper(*args,**kwargs):
#          # "print log before a function"
#          # :param args:
#          # :param kwargs:
#          # :return:
#          print("[DEBUG]{}:enter {}()".format(datetime.date.day,func.__name__))
#          return  func(*args,**kwargs)
#      return  wrapper
#
# @logging
# def say(something):
#       # say something
#       print("say {}!".format(something))

# from functools import wraps
# def logging(func):
#     @wraps(func)
#     def wrapper(*args,**kwargs):
#         """print log before a function"""
#         print("[DEBUG]{}:enter{}()".format(datetime.now(),func.__name__))
#         return func(*args,**kwargs)
#     return wrapper
#
# @logging
# def say(something):
#     """say something"""
#     print("say{}!".format(something))
#
# import inspect


# class Car(object):
#     def __init__(self,model):
#         self.model = model
#
#     @logging #装饰实例方法 OK
#     def run(self):
#         print("{} is running!". format(self.model))
#
#     @logging  #装静态方法， failed
#     @staticmethod
#     def check_model_for(obj):
#         if isinstance(obj,Car):
#             print("The model of your car is {}".format(obj.model))
#         else:
#             print("{} is not a car!".format(obj))

# class Car(object):
#     def __init__(self,model):
#         self.model = model
#
#     @staticmethod
#     @logging #在@staticmethod之前装饰 OK
#     def check_model_for(obj):
#         pass

# #decorator.py
# #先定义包装函数wrapper() 再使用 decorate（func，wrapper) 完成一个装饰器
# def wrapper(func,*args,**kwargs):
#     """print log before a function"""
#     print("[DEBUG]{}:enter {}()".format(datetime.now(),func.__name__))
#     return func(*args,**kwargs)
#
# #wrapper装饰wrapper
# def logging(func):
#   return  decorate(func,wrapper)

#import logging 顶部引入
# #root logger的level是logging.WARNING,低于该级别的就不输出了
# logging.debug(u"苍")
# logging.info(u"麻")
# logging.warning(u"小泽")
# logging.error(u"桃谷")
# logging.critical(u"罗拉")

#2020-11-25 mobile #logging
#第一步，创建一个logger
# logger = logging.getlogger()
# logger.setLevel(logging.INFO)
# #第二步  创建一个handler,用于写入日志文件
# rq = time.strftime("%Y%m%d%H%M",time.localtime(time.time()))
# log_path =os.path.dirname(os.getcwd())+"/Logs/"
# log_name = log_path+rq+".log"
# logfile = log_name
# fh = logging.FileHandler(logfile,mode ="w")
# fh.setLevel(logging.DEBUG)
#第三步，定义handler的输出格式
# formatter = logging.Formatter("%("asctime)s-%(filename)s[line:%(lineno)d]-%(levelname)s:%(message)s")
# fh.setFormatter(formatter)
#第四步，将logger添加到handler里面
# logger.addHandler(fh)
# #日志
# logger.debug("this is a logger debug message")
# logger.info("this is a logger info message")
# logger.warning("this is a logger warning message")
# logger.error("this is a logger error message")
# logger.critical("this is a logger critial message")



# @decorator
# def logging(func,*args,**kwargs):
#     print("[DEBUG]{}:enter{}()".format(datetime.now(),func.__name__))
#     return func(*args,**kwargs)



#装饰器十一  wraps
# from functools import wraps
#
# def wrapper(func):
#     @wraps(func)
#     def inner_function():
#         pass
#     return inner_function
# @wrapper
# def wrapped():
#     pass
#
# print(wrapped.__name__)
# # wrapped
#wraps 偏函数对象
# def wraps(wrapped,
#           assigned = WRAPPER_ASSIGNMENTS,
#           updated = WRAPPER_UPDATES):
#     return partial(update_wrapper, wrapped=wrapped,
#                    assigned=assigned, updated=updated)
# 可以看到wraps其实就是调用了一个函数update_wrapper，知道原理后，我们改写上面的代码，在不使用 wraps的情况下，也可以让wrapped.__name__ 打印出 wrapped，代码如下：
from functools import update_wrapper
#
# WRAPPER_ASSIGNMENTS = ('__module__', '__name__', '__qualname__', '__doc__',
#                        '__annotations__')

# def wrapper(func):
#     def inner_function():
#         pass
#
#     update_wrapper(inner_function, func, assigned=WRAPPER_ASSIGNMENTS)
#     return inner_function
#
# @wrapper
# def wrapped():
#     pass
#
# print(wrapped.__name__)

if __name__ == "__main__":

    # 装饰器一
    # say_hello = debug( say_hello )
    #  say_hello()

    # 装饰器二
    #  say_hello()

    # 装饰器三
    #  say("hr")

    # 装饰器四
    # say("helloworld")

    # 装饰器五(1)
    #  say("hello world")
    # warn("nihao,kitty")
    # do("my work")

    # 装饰器五（2）
    # say("nihao")

    # 装饰器六 基于类实现的装饰器 它必须接受一个callable对象作为参数，
    # 然后返回一个callable对象，一般callable对象都是函数但也有例外，只要重载了__call__()
    # 那么这个对象就是callable
    # t=Test()
    # t()

    # 装饰器七 类初始化一函数，重载返回一函数
    # say("level")

    # 装饰器八 #装饰器八  带参数的类装饰器
    # 如果需要通过类形式实现带参数的装饰器
    # 构造函数里接受的不是一函数，而是传入的参数
    # 通过类把这些参数保存起来，然后重载__call__就是需要接受一个函数并返回一个函数
    # say("hello debug level")

    # 装饰器九 内置的装饰器
    #其实它返回的并不是一个 callable对象，而是一个staticmethod 它是不符合
    #装饰器要求的（比如传入一个callable对象，你自然不能在它之上加别的装饰器
    #要解决这个问题简单，只要把你的装饰器放在@staticmethod之前就好了，因为你的
    #装饰器返回的还是一正常的函数 然后再加上一个@staticmethod是不会出问题的
    # hello()
    html_hello()
    html_hello()

    # 装饰器十 #wrapper  say = logging(say)
    # logging 其实返回的函数名字刚好是wrapper,那么say 语句刚好把结果负值给 say,
    # sayd __name__自然也就是wrapper了,不仅仅是name,其他属性也都来自 wrapper,
    # print( "say.__name__" )

    #装饰器十 functools 函数
    # print(say.__name__) #say
    # print(say.__doc__)  #say something
    # 函数签名和源码还是拿不到的

    # print(inspect.getsource(say))

    # #打开excel文件读取数据
    # data = xlrd.open_workbook("xlrd测试表.xls")
    # #获取所有sheet名称
    # sheet_name = data.sheet_names()
    # #没想到Sheet3也有获取到sheeet3
    # print(sheet_name)
    #
    # #根据下标获取sheet名称
    # sheet2_name = data.sheet_names()[1]
    # print(sheet2_name)
    #
    # #根据 sheet索引或者名称获取sheet内容同时获取名称 行数 列数
    # sheet2 = data.sheet_by_index(1)
    # print("sheet2名称：{}\n sheet2列数：{}\nsheet2行数：{}".format(sheet2.name,sheet2.ncols,sheet2.nrows))
    # #sheet2名称：银行3
    # #sheet2列数：7
    # #sheet2行数：4
    # #根据sheet名称获取整行和整列的值
    # print("<------------>")
    # ##huoyang  为什么这边不使用sheet_names
    # sheet1 = data.sheet_by_name("bank2")
    # print(sheet1.row_values(3))
    # print(sheet1.col_values(3))
    # print( "<------------>" )
    #
    # #获取指定单元格的内容
    # print(sheet1.cell(1,0).value)
    # print(sheet1.cell_value(1,0))
    # print(sheet1.row(1)[0].value)
    # print("hello")