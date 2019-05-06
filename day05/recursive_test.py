
def fn_recursive(n):
    if n == 1:
        return 1
    else:
        return n * fn_recursive(n - 1)


print(fn_recursive(4))


def fn_fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fn_fibonacci(n - 1) + fn_fibonacci(n - 2)


print(fn_fibonacci(10))
