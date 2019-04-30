import os

from urllib.request import urlopen
# f = open('c:/offline_FtnInfo.txt',encoding='utf-8')
# print(f.read())
# f.close()
with open ('c:/offline_FtnInfo.txt',encoding='utf-8')as f:
    print(f.read(3))

with open ('c:/offline_FtnInfo.txt',encoding='utf-8')as f:
    line =  f.readline()
    while line:
        print(line.strip())
        line = f.readline()

s = " 你好，Hello,World!"
print(s.strip())
print(s.lstrip())
print(s.rstrip())

with open('c:/offline_FtnInfo.txt',encoding='utf-8')as f:
    for x in f:
        print(x.strip())

with open('C:/offline_FtnInfo.txt',encoding='utf-8')as f:
    for line in f.readlines():
        print(line.strip())

print(os.getcwd())

with open('1.jpg','rb')as f:
    print(f.read())

with urlopen('https://book.douban.com/tag/%E5%B0%8F%E8%AF%B4')as f:
    for line in f.readlines():
        line = line.decode('utf-8')
        if 'img class=""'in line:
            print(line.strip()[len('<img class="" src="'):len(line.strip())-1])



