def power(x):
    return x * x


print(power(3))


def power(x, n=3):
    p = 1
    while n > 0:
        p *= x
        n -= 1
    return p


print(power(2))


def fn_append(array=None):
    if array is None:
        array = []
    array.append('END')
    return array


print(fn_append([1, 2, 3]))

print(fn_append())
print(fn_append())

print(max(1, 2, 3, 4))


def fn_sum(*numbers):
    print(numbers)
    s = 0
    for n in numbers:
        s += n
    return s


print(fn_sum(1, 2, 3, 4))

num = (1, 2, 3, 4)
print(fn_sum(*num))


def fn_test(a, b=1, *c, d, **e):
    print(a, b, c, d,e)

fn_test(1,2,123,'abc',d='456',married='False')

