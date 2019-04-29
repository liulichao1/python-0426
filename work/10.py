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