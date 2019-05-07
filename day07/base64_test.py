# @Time : 2019/5/7 14:57
# @Author : 2273360936@qq.com
# @FileName : base64_test.py
# @GitHub : https://github.com/liulichao1/python-0426
import base64

s = b'Hello, World!'
print(base64.encodebytes(s))
print(base64.decodebytes(b'SGVsbG8sIFdvcmxkIQ==\n'))