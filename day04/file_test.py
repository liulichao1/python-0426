import os
import shutil

if os.path.exists('test.txt'):
    os.remove('test.txt')
else:
    print('not exits.')

#os.rename('download.py','down_test.py')

#shutil.copy('file_test.py','new_flie_test.py')

# if os.path.exists('new_flie_test.py'):
#     os.remove('new_flie_test.py')

print([x for x in os.listdir('.')if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])

print(os.path.splitext('file_test.py'))