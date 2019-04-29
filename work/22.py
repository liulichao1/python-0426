#22. 利用递归方法求5!

def fact(i):
    sum = 0
    if i == 0:
        sum = 1
    else:
        sum = i*fact(i-1)
    return sum

print(fact(5))