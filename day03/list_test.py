names = ['Tom','Jerry','Mike']
print(names[0])

names.append('Mary')
print(names)

names.insert(2,'Tyke')
print(names)

names.pop()
print(names)

superstars = ['Hero','iron man']
names = superstars.copy()
print(names)

names[1]='Iron Man'
print(names)

names.remove('Hero')
print(names)

names.sort(reverse=True)
print(names)

for name in names:
    print(name)
#1. 求一个数值 list 的所有元素和
nums = [12,23,34,45]
print(sum(nums))

#2. 求一个数值 list 的最大/最小元素值
print(max(nums))
print(min(nums))

#3. 求一个字符串 list 中，字符串长度大于2，且首尾字符相同的元素个数
a = ['a', 'xy', 'alabama', '101']
counter = 0
for s in a:
    if (len(s) > 2) & (s[0] == s[-1]):
        counter = counter+1
print(counter)


