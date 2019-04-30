
#1. 求一个数值 list 的所有元素和
nums = [12,23,34,45]
print(sum(nums))

#2. 求一个数值 list 的最大/最小元素值
print(max(nums))
print(min(nums))

#3. 求一个字符串 list 中，字符串长度大于2，且首尾字符相同的元素个数
a = ['a', 'xy', 'alabama', '101']
counter = 0
for s in a:
    if (len(s) > 2) & (s[0] == s[-1]):
        counter = counter+1
print(counter)

#4. 把一个 tuple 转为字符
t = ('abc','123456','xyz')
for i in t:
    print(i)

#5. 对一个 tuple 进行各种切片操作
print(t[0:2])
print(t[2])

#6. 把 3 个 dict 合并为 1 个 dict
x = {'a':1, 'b': 2}
y = {'c': 3,'d':4}
z = {'e':5,'f':6}
m =x.update(y)
n = x.update(z)
print(x)

# 7. 把一个 dict 按 key 排序输出
import collections
d = collections.OrderedDict()
d = {'k1': 'v1', 'k2': 'v2'}
for key in d:
    print(key,':',d[key])

# 8.找出两个 dict 中的 key-value 相同项
q={'key1':1,'key2':5,'key3':2}
w={'key1':1,'key2':2}
print(q.items() & w.items())
print(q.keys() & w.keys())

# 9. 求一个 set 的大/小元素值
keys = {'1', '12', '123', '1234'}
print(max(keys))
print(min(keys))

# 10. 把两个 set 中的不同元素构造为一个新的 set 并输出
a = {11, 22, 33, 44}
b = {44, 22, 33, 55}
c = a ^ b
print(c)
print(a.symmetric_difference(b))