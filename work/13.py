#13. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math

for z in range(10000):
    x =int(math.sqrt(100+z))
    y = int(math.sqrt(268+z))
    if(x*x == (100+z))and(y*y == (z+268)):
        print(z)
