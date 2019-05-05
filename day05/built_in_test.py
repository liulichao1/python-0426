print(dir('__builtins__'))

print(abs(-3))

print(min(1, -3, -2, 9))

print(str(123) + 'test')

a = [1, 2, 3, 1, 2, 3]

b = tuple(a)

print(b)

c = set(a)

print(c)

d = set(b)

print(c, d)

print(type(a), type(b), type(c), type(d))


def add(x, y):
    return x + y


print(add(123, 6869))


def multi_return(x, y):
    """
    :param x: int...
    :param y: float...
    :return: tuple...
    """
    return x, y


m, n = multi_return(12, 34)

print(m, n)

print(multi_return(12, 34))
