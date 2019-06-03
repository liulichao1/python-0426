import numpy as np
from 逻辑回归 import data_reader
from 逻辑回归 import show

def sigmoid(x):
    return 1.0 / (1 + np.exp(-x))


def get_cost(theta, x, y):
    h = sigmoid(np.dot(x, theta))
    cost = np.sum(y * np.log(h) + (1 - y) * np.log(1 - h))
    return -cost


def get_grade(theta, x, y):
    h = sigmoid(np.dot(x, theta))
    return np.dot(np.transpose(x), h - y)


def decay_learning_rate(learning_rate,decay_rate,ecphocs):
    return learning_rate / (decay_rate * ecphocs + 1)


def graident_descending(theta, x, y, learning_rate, batch_size, ecphocs=20):
    global cost
    costs = []
    learning_rates = []
    batchs = len(x) // batch_size
    if len(x) % batch_size != 0:
        batchs += 1
    for ephoc in range(ecphocs):
        for batch in range(batchs):
            start = batch * batch_size % len(x)
            end = min(start + batch_size, len(x))
            t_x = x[start:end]
            t_y = y[start:end]
            theta = theta - learning_rate * get_grade(theta, t_x, t_y)
            cost = get_cost(theta, x, y)
        costs.append(cost)
        learning_rate = decay_learning_rate(learning_rate, 0.99, ephoc)
        learning_rates.append(learning_rate)
    show.show_cost(costs)
    show.show_cost(learning_rates)


x, y = data_reader.read_data()
theta = np.zeros((x.shape[1], 1))
learning_rate = 0.0001
graident_descending(theta, x, y, learning_rate, batch_size=10)
