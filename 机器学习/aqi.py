# @Time : 2019/5/21 10:47
# @Author : 2273360936@qq.com
# @FileName : aqi.py
# @GitHub : https://github.com/liulichao1/python-0426
import numpy as np
import read_data
from show import show_cost


def get_grad(theta, x, y):
    grad = np.dot(np.transpose(x), (np.dot(x, theta) - y))
    return grad


def gradient_descending(theta, x, y, v_x, v_y, learning_rate):
    # costs = []
    # 通过梯度下降算法，对线性回归模型进行训练
    train_costs = []
    validation_costs = []
    for _ in range(200):
        theta = theta - get_grad(theta, x, y) * learning_rate
        train_costs.append(get_cost(theta, x, y))
        validation_costs.append(get_cost(theta, v_x, v_y))
    show_cost(train_costs, validation_costs)
    with open("model.txt", "w")as f:
        for i in theta:
            for j in i:
                f.writelines(str(j) + '\n')
    return theta


def test_model(theta, test_x, test_y):
    # 使用R方误差来测试模型的优劣
    r = 1 - get_cost(theta, test_x, test_y) / np.var(test_y)
    print(r)


def get_cost(theta, x, y):
    # x:是一个矩阵
    # y:是一个矩阵
    # theta:是一个矩阵
    return np.mean((np.dot(x, theta) - y) ** 2)


def get_aqi_value(input_data):
    #  根据用户提供的输入数据，完成aqi值的预测
    x = np.array(input_data)
    x = read_data.standard_data(x)
    with open('model.txt', 'r')as f:
        theta = np.array([float(line) for line in f.readlines()]).reshape(6, 1)

    return np.dot(x, theta)


# x, y = read_data.read_aqi()
train_data, validation_data, test_data = read_data.read_aqi()

theta = np.zeros((6, 1))
learning_rate = 0.00003

# gradient_descending(theta, x, y, learning_rate)
theta = gradient_descending(theta, train_data[0], train_data[1], validation_data[0], validation_data[1], learning_rate)
aqi_value = get_aqi_value([41, 66, 9, 38, 1.11, 112])
print(aqi_value)
