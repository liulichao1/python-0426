with open('test.txt','w')as f:
    f.write("你好hello1")

with open('test.txt','a')as f:
    f.write("你好hello2")

with open('1.jpg','rb')as f1:
    with  open('2.jpg','wb')as f2:
        f2.write(f1.read())