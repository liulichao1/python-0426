# @Time : 2019/5/21 10:47
# @Author : 2273360936@qq.com
# @FileName : aqi.py
# @GitHub : https://github.com/liulichao1/python-0426
import numpy as np
import read_data
from show import show_cost


def get_grad(theta, x, y):
    grad = np.dot(np.transpose(x), (np.dot(x, theta)-y))
    return grad


def gradient_descending(theta, x, y, learning_rate):
    costs = []
    for _ in range(200):
        theta = theta - get_grad(theta, x, y) * learning_rate
        costs.append(get_cost(theta, x, y))
    show_cost(costs)


def get_cost(theta, x, y):
    return np.mean((np.dot(x, theta) - y) ** 2) * 0.5


x, y = read_data.read_aqi()
theta = np.zeros((6, 1))
learning_rate = 0.00000001
gradient_descending(theta, x, y, learning_rate)
