# @Time : 2019/5/10 10:18
# @Author : 2273360936@qq.com
# @FileName : douban_top250.py
# @GitHub : https://github.com/liulichao1/python-0426
import requests
import re
from lxml import etree


def parse(url):
    # 得到HMTL文档
    html = requests.get(url)

    # 解析文档
    # 获取豆瓣top250中页面的标题
    selector = etree.HTML(html.text)
    #  print(html.text)
    all_movies = []

    movies_list = selector.xpath("//ol[@class='grid_view']/li")

    for movie_selector in movies_list:
        name = movie_selector.xpath(".//div[@class='hd']/a/span[1]/text()")[0]  # 名称
        director_and_act = movie_selector.xpath(".//div[@class='bd']/p[1]/text()")[0].strip("\n").strip(" ")  # 导演和主演
        director = re.findall("导演: (.*?) ", director_and_act)[0]
        act = re.findall("主演: (.*?) ", director_and_act)
        if not act:
            act = ["未知"]

        star = movie_selector.xpath(".//div[@class='star']/span[@class='rating_num']/text()")[0]  # 评分
        nums = movie_selector.xpath(".//div[@class='star']/span[last()]/text()")[0]  # 人数
        #  nums = nums.split("人评价")[0]
        nums = re.sub("\D", "", nums)
        url = movie_selector.xpath(".//div[@class='hd']/a/@href")[0]  # 地址
        one_movie = [name, director, act[0], star, nums, url]

        all_movies.append(one_movie)
    print(all_movies)

    for movie in all_movies:
        one_str = movie[0] + ',' + movie[1] + ',' + movie[2] + ',' + movie[3] + ',' + movie[4] +','+movie[5]+ "\n"
        with open("movies.txt", "a", encoding="utf-8")as f:
            f.write(one_str)

    next_url = selector.xpath("//span[@class='next']/a/@href")
    if next_url:
        next_url = "https://movie.douban.com/top250" + next_url[0]
        parse(next_url)


if __name__ == "__main__":
    parse("https://movie.douban.com/top250")
