# @Time : 2019/5/13 9:36
# @Author : 2273360936@qq.com
# @FileName : notes2.py
# @GitHub : https://github.com/liulichao1/python-0426
import requests
from lxml import etree

header = {  # 字典型
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/70.0.3538.110 Safari/537.36"}

with open("cookie.txt", "r", encoding="utf-8") as f:
    cookies_str = f.readline()

# 将cookies字符串转换为字典型
cookie_list = cookies_str.split(";")
cookie_dict = {}
for cookie in cookie_list:
    key = cookie.split("=")[0].replace(" ", "")
    value = cookie.split("=")[1]
    cookie_dict[key] = value

html = requests.get("https://www.douban.com/people/196409155/notes", headers=header, cookies=cookie_dict)
print(html.text)
