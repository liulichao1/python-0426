# @Time : 2019/5/7 14:43
# @Author : 2273360936@qq.com
# @FileName : pillow_test.py
# @GitHub : https://github.com/liulichao1/python-0426
from PIL import Image, ImageFilter

image = Image.open('1.jpg')
w, h = image.size
image.thumbnail((w // 2, h // 2))
image.save('new.jpg')

image = Image.open('1.jpg')
image_blur = image.filter(ImageFilter.BLUR)
image_blur.save('blur.jpg')
