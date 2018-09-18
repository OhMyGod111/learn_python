#!/usr/bin/python3
import pickle
import pprint
import os
import sys

'''
a = "hello world!"
str(a)
'''

# str.format() 的基本使用如下:
print('{}网址： "{}!"'.format('菜鸟教程', 'www.runoob.com'))

# 关键字
print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# 按位置
print('{0} 和 {1}'.format('Google', 'Runoob'))

#  读取键盘输入
str = input("请输入：");
print ("你输入的内容是: ", str)

# 读和写文件 打开一个文件
f = open(sys.path[1]+'/tmp/foo.txt', "w")

f.write(str)

# 关闭打开的文件
f.close()


# 打开一个文件 读文件
f = open(sys.path[1]+'/tmp/foo.txt', "r")

str = f.readline()
print(str)

# 关闭打开的文件
f.close()

# 简写方式
read_data = ""
with open(sys.path[1]+'/tmp/foo.txt', 'r') as f:
    read_data += f.read()
print("获取到的内容：",read_data)    
f.closed

# 使用pickle模块将数据对象保存到文件
data1 = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

output = open('data.pkl', 'wb')

# Pickle dictionary using protocol 0.
pickle.dump(data1, output)

# Pickle the list using the highest protocol available.
pickle.dump(selfref_list, output, -1)

output.close()


#使用pickle模块从文件中重构python对象
pkl_file = open('data.pkl', 'rb')

data1 = pickle.load(pkl_file)
pprint.pprint(data1)

data2 = pickle.load(pkl_file)
pprint.pprint(data2)

pkl_file.close()


if __name__ == '__main__':
	pass

else:
	print("我被别的模块所引用")