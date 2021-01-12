# -*- coding: utf-8 -*-
# @Time    : 
# @Author  : huoyanyang
# @Site    : 
# @File    : 
# @Software: PyCharm
from selenium import  webdriver

driver = webdriver.Firefox()
driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols")

ele_framest = driver.find_element_by_css_selector("#result>iframe")
driver.switch_to.frame(ele_framest)

# 切换到第二个子类frame
driver.switch_to.frame(1)
# 最上层
driver.switch_to.default_content()
print(driver.page_source)