
import sys
print("Hello, World! --------------------------------------->")

# input("\n\n按下 enter 键后退出。")
# 基本数据类型
a = 10

b = 2.12

j = 3

c = 1 + 2 * j 

str1 = "hello Python"

# print("a=" + a +";b="+b+";c="+c)
print(a)
print(c)
print(str1)

# 数据类型判断
print(type(a), type(b), type(c), type(str1))
print(isinstance(a,int),isinstance(b,float),isinstance(j,complex))

# 导入 sys 模块
print('================Python import mode==========================');
print ('命令行参数为:')
for i in sys.argv:
    print (i)
print ('\n python 路径为',sys.path)



#导入 sys 模块的 argv,path 成员
from sys import argv,path  #  导入特定的成员
 
print('================python from import===================================')
print('path:',path) # 因为已经导入path成员，所以此处引用时不需要加sys.path

print(int('10016'))
