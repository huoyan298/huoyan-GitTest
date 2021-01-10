# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from time import  sleep


# 模拟鼠标操作-拖动-滑动验证码
driver = webdriver.Firefox()
driver.get("https://www.taobao.com/")
sleep(1)

#获取悬浮的元素
element_list = driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[1]/div[1]/span[1]")
ActionChains(driver).move_to_element(element_list).perform()
driver.find_element_by_xpath("/html/body/div[1]/div[1]/div/ul[1]/li[1]/div[2]/ul/li[4]").click()
