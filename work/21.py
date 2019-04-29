#21. 求1+2!+3!+…+20!的和。

t = 1
s = 0
for n in range(1,21):
    t *= n
    s += t
print(s)
