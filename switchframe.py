# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from  selenium  import webdriver
from time import sleep
from logging import log

driver = webdriver.Firefox()

driver.get("https://www.baidu.com/")

driver.find_element_by_xpath("//*[@id='s-top-left']/a[2]").click()
all = driver.window_handles

now_page = driver.current_window_handle

driver.switch_to.window(all[1])
title_page =driver.title
sleep(2)
driver.close()
# 切换回另一个页签窗口
driver.switch_to.window()