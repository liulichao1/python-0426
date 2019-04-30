import os
print(os.path.abspath('.'))

print(os.getcwd())

print(os.path.join('d:/test1','test2','test.txt'))

# print(os.makedirs(os.path.join('.','new_dir','sub_dir')))

#print(os.rmdir(os.path.join('.','new_dir')))

print(os.path.split('new_dir/sub_dir/test.txt'))

print(os.path.splitext('google.com.png'))

print([x for x in os.listdir('.')if os.path.isfile(x)])
