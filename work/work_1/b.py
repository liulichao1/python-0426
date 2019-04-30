import re
# 1. 读取一个文本文件的前 N 行
with open('c:/offline_FtnInfo.txt',encoding='utf-8')as f:
    for x in f:
        print(x.strip())

# 2. 按行读取一个文件，把每行内容存入一个 list

result=[]
with open('c:/offline_FtnInfo.txt','r') as f:
 for line in f:
     result.append(list(line.strip('\n').split(',')))
print(result)

# 3. 查询一篇英文文章的最长单词
text=['[', 'Paradise', 'Lost', 'by', 'John', 'Milton', '1667', ']', 'Book', 'I', 'Of', 'Man', "'", 's', 'first', 'disobedience', ',', 'and', 'the', 'fruit']
longest = ''
for word in text:
   if len(word) > len(longest):
       longest = word
print(longest)

# 4. 找出一片英文文章的最高频单词
from collections import Counter
from matplotlib.pyplot import pie,show
f = 'c:/offline_FtnInfo.txt'
c = Counter(re.findall(r'(\w{3,})',open(f).read().lower())).most_common(3)
pie([i[1] for i in c],labels=[i[0] for i in c])
show()



