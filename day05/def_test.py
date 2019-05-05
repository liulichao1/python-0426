from day05.built_in_test import multi_return

print(multi_return(34, 56))


def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('Error...')
    if x > 0:
        return x
    else:
        return -x


print(my_abs('-3'))
print(my_abs(-3))
