"""
20. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。

"""
sum = 0
a, b = 2, 1
for i in range(20):
    sum = sum + a/b
    a = a + b
    b = a - b
print(sum)
