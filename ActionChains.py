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
driver.get("https://reg.taobao.com/member/reg/fill_mobile.htm")
driver.maximize_window()

# 点击确定
element_confirm = driver.find_element_by_css_selector("#J_AgreementBtn")
element_confirm.click()
sleep(1)
# 获取模块条size
span_background = driver.find_element_by_css_selector("#nc_1__scale_text > span")
span_background_size =span_background.size
print(span_background_size)
# 获取滑块位置
span_btn_background =driver.find_element_by_css_selector("#nc_1_n1z")
span_btn_location = span_btn_background.location
print(span_btn_location)

#nc_1__scale_text > span:nth-child(1)
# 拖动操作 drag_and_drop_by_offset
x_location = span_btn_location["x"]+span_background_size["width"]
y_location = span_btn_location["y"]
ActionChains(driver).drag_and_drop_by_offset(span_btn_background,x_location,y_location).perform()
