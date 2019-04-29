d ={'k1':'v1','k2':'v2'}
print(d)

d = {}.fromkeys('k1','v1')
print(d)

d={'key':'value'}
print(d['key'])
print(d.get('key1'))
print(d.get('key1','new vale'))

d = {'name':'Tom','age':18,'married':'False'}
print(d)

import collections

d = collections.OrderedDict()
d = {'k1':'v1','k2':'v2'}
for key in d:
    print(key,d[key])
for key in d:
    print(key,d[key])

for k,v in d.items():
    print(k,v)