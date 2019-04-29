tup = ('Hello','World')
print(tup)

numbers = (1,)
print(numbers)

print(len(numbers))

names = tuple(('test','test'))
print(names.count('test'))
print(names.index('test'))

superstars = ['Tom','Jerry']
names = (superstars,'Spike')
print(names)

names[0].append('Mike')
print(names)

for name in names:
    print(name)