#!/usr/bin/python3

from src.utils import line_util

line_util.cuttingLine("数据结构")

line_util.cuttingLine("列表操作")

a = [66.25, 333, 333, 1, 1234.5]
print(a.count(333), a.count(66.25), a.count('x')) # 返回 x 在列表中出现的次数。

a.insert(2, -1) # 插入
print(a)
a.append(333)  # 追加
print(a)

line_util.cuttingLine("将列表当做堆栈使用")

stack = [3, 4, 5]
stack.append(6)
stack.append(7)
print(stack)

stack.pop()
print(stack)

stack.pop(0)
print(stack)


line_util.cuttingLine("将列表当作队列使用")

from collections import deque
queue = deque(["Eric", "John", "Michael"])
queue.append("Terry")           # Terry arrives
queue.append("Graham")          # Graham arrives
print(queue)
a = queue.popleft()
print(a)
print(queue) 

line_util.cuttingLine("元组和序列")

t = 12345, 54321, 'hello!'
print(t[0])
(12345, 54321, 'hello!')
# Tuples may be nested:
u = t, (1, 2, 3, 4, 5)
print(u)

line_util.cuttingLine("集合")

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 删除重复的

'orange' in basket                 # 检测成员
print("True")
'crabgrass' in basket
print("False")

# 以下演示了两个集合的操作
a = set('abracadabra')
b = set('alacazam')
print(a)                                  # a 中唯一的字母
print(a - b)                              # 在 a 中的字母，但不在 b 中

print(a | b)                              # 在 a 或 b 中的字母
print(a & b)                              # 在 a 和 b 中都有的字母
print(a ^ b)                              # 在 a 或 b 中的字母，但不同时在 a 和 b 中

c = set({1,2,3,23,22,77,564,45,67})
d = set({"网","易","云","音","乐"})

print(c)
print(d)

e = set()
# e = {}  # 申明空集合不能使用{}  因为{}是申明空字典用的  只能使用 set() 语法

for x in range(1,10):
	e.add(x)

print(e)


line_util.cuttingLine("列表推导式")

vec = [2, 4, 6]
value = [3*x for x in vec]
print(vec,end = "       <---vec \n")

print(value,end = "     <---value \n")

value1 = [[x, x**2] for x in vec]
print(value1,end = "    <---value1 \n")


a = {x for x in 'abracadabra' if x not in 'abc'}
print(a,end = "         <---集合推导 \n")


b = {x: x**2 for x in (2, 4, 6)}
print(b,end = "    <---字典推导 \n")

line_util.cuttingLine("字典")

tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127
print(tel)
del tel['sape']
tel['irv'] = 4127
print(tel)

print(sorted(tel.keys())) # 排序

print(list(tel.keys())) 
print('guido' in tel) 


line_util.cuttingLine("字典遍历技巧")

knights = {'gallahad': 'the pure', 'robin': 'the brave'}
for k, v in knights.items():
    print(k, v)

# 遍历序列  enumerate()  函数将下标 和 对应的值遍历出来
for i, v in enumerate(['tic', 'tac', 'toe']):
     print(i, v)

# 同时遍历两个或更多的序列，可以使用 zip() 组合：

questions = ['name', 'quest', 'favorite color']
answers = ['lancelot', 'the holy grail', 'blue']
for q, a in zip(questions, answers):
    print('What is your {0}?  It is {1}.'.format(q, a))
