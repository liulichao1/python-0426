# @Time : 2019/5/7 10:56
# @Author : 2273360936@qq.com
# @FileName : collections_test.py
# @GitHub : https://github.com/liulichao1/python-0426
from collections import namedtuple, deque, defaultdict, OrderedDict, Counter

Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)
print(isinstance(p, Point))
print(isinstance(p, tuple))
Circle = namedtuple('Circle', ['x', 'y', 'r'])
c = Circle(1, 2, 3)
print(c.x)
print(c.y)
print(c.r)
print(c._asdict())
# c.x = 0
# deque
q = deque([1, 2, 3])
print(q.pop())
print(q.popleft())
q.appendleft(1)
print(q)
q.append(3)
print(q)


# defaultdict
def na():
    return 'N/A'


d = defaultdict(na)
# d = defaultdict(lambda: 'N/A')
d['key'] = 'value'
print(d['key'])
print(d['k'])
# OrderedDict
d = dict([(1, 'x'), (2, 'y'), (3, 'z')])
print(d)
d = OrderedDict([(1, 'x'), (2, 'y'), (3, 'z')])
print(d)
d[-1] = 'a'
d[-2] = 'b'
d[-3] = 'c'
print(d)
# Counter
counter = Counter()
for c in 'programming':
    counter[c] += 1
print(counter)
words = ['hello', 'world', 'nice', 'world']
counter = defaultdict(lambda: 0)
for word in words:
    counter[word] += 1
print(counter)
