#15. 输入三个整数x，y，z，请把这三个数由小到大输出。
numbers = []
for i in range(4):
    if i > 0:
        x = int(input(f"请输入第{i}个整数："))
        numbers.append(x)
print("由小到大排序完后是：",sorted(numbers))