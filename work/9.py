#9.一个数如果恰好等于它的因子之和，这个数就称为’完数’。例如6=1＋2＋3.编程 找出1000以内的所有完数。
for i in range(1,1001):
    sum = 0
    for j in range(1,i):
        #判断是否因子,是因子 求和
        if (i%j ==0): sum += j
    if (sum == i):
        print ("完数：",i)

#10. 一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？
high = 100
n = 10
high_all = 0 #第n次落地时走过的长度
high_each = 0 #每次落地的高度


def ball_lands(n):
    global high_all, high_each, high
    #小球第一次落地时
    if n == 0:
        high_each = high
        high_all += high_each
        #print('1', high_each, high_all)
        return high_each
    #从小球第n次落地往前推
    high_each = high * (1 / 2) ** n
    print('第%d次小球弹起的高度为：%.2f' %(n, high_each))
    high_all += high_each * 2
    #print('2', high_each, high_all)
    ball_lands(n - 1)

ball_lands(n)
print('小球落地%d次，共经过%.2f米。' % (n,high_all))


#13. 一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
import math

for z in range(10000):
    x =int(math.sqrt(100+z))
    y = int(math.sqrt(268+z))
    if(x*x == (100+z))and(y*y == (z+268)):
        print(z)

'''14. 输入某年某月某日，判断这一天是这一年的第几天？(闰年： 西元年份除以400余数为0的，或者除以4为余数0且除以100不为余数0的，为
闰年。)
'''
import datetime

y = int(input('请输入4位数字的年份：'))  #获取年份
m = int(input('请输入月份：'))  #获取月份
d = int(input('请输入是哪一天：'))  #获取“日”

targetDay = datetime.date(y, m, d)  #将输入的日期格式化成标准的日期
print(targetDay - datetime.date(targetDay.year-1, 12, 31))  #减去上一年最后一天，可得解

#15. 输入三个整数x，y，z，请把这三个数由小到大输出。
numbers = []
for i in range(4):
    if i > 0:
        x = int(input(f"请输入第{i}个整数："))
        numbers.append(x)
print("由小到大排序完后是：",sorted(numbers))

#16. 输出9*9口诀。
for i in range(1,10):
    for j in range(1,i+1):
        print(str(j)+ str('*')+str(i)+"="+str(i*j),end="\t")
    print()

#19.1.把菱形分解为上下两部分
#   2.分析每部分的规律
#   3.使用循环进行输出
for i in range(1,5):
    for j in range(4-i,0,-1):
        print(' ',end='')
    for k in range(0,(i-1)*2):
        print('x',end='')
    print('x')

for i in range(1,4):
    for j in range(0,i):
        print(' ',end='')
    for k in range(4,(i-1)*2,-1):
        print('x',end='')
    print('x')

"""
20. 有一分数序列：2/1，3/2，5/3，8/5，13/8，21/13…求出这个数列的前20项之和。

"""
sum = 0
a, b = 2, 1
for i in range(20):
    sum = sum + a/b
    a = a + b
    b = a - b
print(sum)

#21. 求1+2!+3!+…+20!的和。

t = 1
s = 0
for n in range(1,21):
    t *= n
    s += t
print(s)

#22. 利用递归方法求5!

def fact(i):
    sum = 0
    if i == 0:
        sum = 1
    else:
        sum = i*fact(i-1)
    return sum

print(fact(5))

#53. 请根据 BMI 公式，根据用户输入计算 BMI 指数，并输出测试结果weight kg  height m
#<= 18 过轻(18, 25] 正常(25, 28] 过重(28, 32] 肥胖> 32 严重肥胖
name = input('Name')

height = input('Height(m):')

weight = input('Weight(kg):')

BIM = float(float(weight) / (float(height) **2))

if BIM < 18.5:

    print('过轻')

elif BIM <= 25:

    print('正常')

elif BIM <= 28:

    print('过重')

elif BIM <= 32:

    print('肥胖')

else:

    print('严重肥胖')
