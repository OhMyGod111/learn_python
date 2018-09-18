#!/usr/bin/python3

print("----------------------作用域------------------------------------------")


class Person(object):
	"""docstring for Person"""
	def __init__(self):
		super(Person, self).__init__()

	a = 100





prson = Person()
print(prson)
print(prson.__class__)

print(prson.a)

if 1==1:
	b = 200

print(b)	


print("\n")
print("----------------------全局变量和局部变量1---------------------------------------")


total = 0 # 这是一个全局变量
# 可写函数说明
def sum(arg1, arg2 ):
    #返回2个参数的和."
    global total  # global 关键字声明全局变量
    total = arg1 + arg2 # total在这里是局部变量.
    print ("函数内是局部变量 : ", total)
    return total
 
#调用sum函数
sum( 10, 20 )
print ("函数外是全局变量 : ", total)
		
print("\n")
print("----------------------全局变量和局部变量2---------------------------------------")

def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明 闭包作用域是使用
        num = 100
        print(num)
    inner()
    print(num)
outer()



print("\n")
print("----------------------全局变量和局部变量3---------------------------------------")

# 出错代码
"""
a = 10       
def test():
    a = a + 1
    print(a)
test()
"""

'''
改造上面代码
'''
a = 10       
def test(a):
    a = a + 1
    print(a)
test(a)



'''
x = int(2.9)  # 内建作用域
 
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''