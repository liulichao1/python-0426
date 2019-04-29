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
