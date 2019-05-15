# @Time : 2019/5/15 16:13
# @Author : 2273360936@qq.com
# @FileName : douban_selenium.py
# @GitHub : https://github.com/liulichao1/python-0426
from selenium import webdriver
import time
#  声明浏览器对象
driver = webdriver.Chrome()
driver.get("https://movie.douban.com/")
a = driver.find_element_by_xpath(".//div[@class='nav-items']/ul/li[2]/a")
a.click()
time.sleep(3)

more_button = driver.find_element_by_class_name("more")
for i in range(5):
    more_button.click()
    time.sleep(3)

from lxml import etree

selector = etree.HTML(driver.page_source)
names = selector.xpath(".//div[@class='list']/a/p/text()")
print(names)