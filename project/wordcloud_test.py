# @Time : 2019/5/7 16:05
# @Author : 2273360936@qq.com
# @FileName : wordcloud_test.py
# @GitHub : https://github.com/liulichao1/python-0426
import matplotlib.pyplot as plt
from wordcloud import WordCloud
import jieba

text_from_file_with_apath = open('c:/offline_FtnInfo.txt').read()

wordlist_after_jieba = jieba.cut(text_from_file_with_apath, cut_all=True)
wl_space_split = " ".join(wordlist_after_jieba)

my_wordcloud = WordCloud().generate(wl_space_split)

plt.imshow(my_wordcloud)
plt.axis("off")
plt.show()
