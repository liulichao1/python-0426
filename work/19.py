#1.把菱形分解为上下两部分
#2.分析每部分的规律
#3.使用循环进行输出
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

