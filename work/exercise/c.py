from functools import reduce


# 定义一个函数，统计字符串中大写和小写的个数
def count(str):
    char_number1 = char_number2 = 0
    for char in str:
        if char.isupper():
            char_number1 += 1
        else:
            char_number2 += 1
    print("大写字母个数：%d,小写字母个数：%d," % (char_number1, char_number2))
    return


count("abcdEFG")

# 定义一个函数，把一个list中的函数去重，返回新的list
x = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
print(list(set(x)))

y = [1, 4, 3, 3, 4, 2, 3, 4, 5, 6, 1]
func = lambda x, y: x if y in x else x + [y]
print(reduce(func, [[], ] + y))


def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(10))


# 汉诺塔
def move(n, a, b, c):
    if n == 1:
        print(a, '->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '->', c)
        move(n - 1, b, a, c)


move(3, 'A', 'B', 'C')


# 打印杨辉三角
def triangles():
    L = [1]  # 定义L为一个只包含一个元素的列表
    while True:
        yield L  # 定义为生成器函数
        L = [1] + [L[n] + L[n - 1] for n in range(1, len(L))] + [1]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


# zip方法
def triangles():
    n = [1]
    while True:
        yield n
        n = [x + y for x, y in zip([0] + n, n + [0])]


n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


# 参数组合练习
def fn_test(a, b=1, *c, d, **e):
    print(a, b, c, d, e)


fn_test(1, 2, 123, 'abc', d='456', married='False')


# 高阶函数练习


def power(x, n=2):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(3))

numbers = [2, 3, 4]

print(list(map(power, numbers)))


def add(x, y):
    return x + y


print(reduce(add, [1, 2, 3, 4, 5]))


# filter()用于过滤序列。例：过滤出奇数
def is_odd(n):
    return n % 2 == 1


tmplist = filter(is_odd, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
newlist = list(tmplist)
print(newlist)

# sorted()对所有可迭代的对象进行排序操作。例：通过 key 的值来进行数组/字典的排序
array = [{"age": 20, "name": "a"}, {"age": 25, "name": "b"}, {"age": 10, "name": "c"}]
array = sorted(array, key=lambda x: x["age"])
print(array)

print(sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'}))
