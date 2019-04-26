import platform
import time
print('Hello,PyCharm!')
#comment
print(0xff)
print('tom\'s name')
print('a','bc','def')
print("""
登 鹳 雀 楼
- 【唐】王之涣

白日依山尽，
黄河入海流。
欲穷千里目，
更上一层楼。
""")
#C:\Users\chao>python
print(platform.python_version())

print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time())))

a=input("please input a:")
b=3.14
area=float(a)*float(a)*float(b)
print(area)

'''isdigit() isnumeric() isdecimal() 的区别
    isdigit()
True: Unicode数字，byte数字（单字节），全角数字（双字节），罗马数字
False: 汉字数字
Error: 无

isdecimal()
True: Unicode数字，，全角数字（双字节）
False: 罗马数字，汉字数字
Error: byte数字（单字节）

isnumeric()
True: Unicode数字，全角数字（双字节），罗马数字，汉字数字
False: 无
Error: byte数字（单字节）
'''
