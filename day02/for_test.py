s = '*'
for i in range(1, 8, 2):
    print((s * i).center(7))
for i in reversed(range(1, 6, 2)):
    print((s * i).center(7))

for j in range(0,10,2):
    print(j)

for k in range(1,8,2):
    print(k)
for m in range(1,6,2):
    print(m)

fruits = ['apple', 'banana', 'orange', 'watermelon']  # list 列表
# fruits = []  # list 列表
for fruit in fruits:
    print(fruit)
    if fruit == 'banana':
        break
else:  # 循环正常结束后的处理：没有 break
    print('else...')

for fruit in fruits:
    print(fruit)
    if fruit == 'watermelon':
        # proceed...
        print('found watermelon.')
        break
# else:  # 循环正常结束后的处理：没有 break
#     print('not found watermelon.')

#编写程序实现：打印出101-200之间的素数
counter = 0
for i in range(101,201):
    for j in range(2,i):
        if i%j == 0:
            break
    else:
          print(i)
          counter = counter + 1
print(counter)

