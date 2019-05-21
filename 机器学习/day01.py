# @Time : 2019/5/21 10:47
# @Author : 2273360936@qq.com
# @FileName : day01.py
# @GitHub : https://github.com/liulichao1/python-0426
import np


def get_grad(theta, x, y):
    grad = 2 * (theta * x - y) * x
    return -grad


def get_cost(theta, x, y):
    # return (theta * x - y) ** 2
    return np.sum((np.dot(x, theta) - y) ** 2)


x = np.array([[1, 2], [1, 2]])
y = np.array([0, 0])
theta = np.array([1, 1])

print(get_cost(theta, x, y))


def gradient_descending(theta, x, y, learning_rate):
    for i in range(20):
        theta = theta + get_grad(theta, x, y) * learning_rate  # 距离相加
        print(get_cost(theta, x, y))


y = 20
x = 1.1
theta = 0
learning_rate = 0.1
gradient_descending(theta, x, y, learning_rate)
# cost = get_cost(theta, x, y)
# print(cost)
# theta = gradient_descending(theta, x, y, learning_rate)
# cost = get_cost(theta, x, y)
# print(cost)
