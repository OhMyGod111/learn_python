#!/usr/bin/python3

print("----------------------分割线------------------------------------------")



list=[1,2,3,4]
# it = iter(list)    # 创建迭代器对象
for x in list:
    print (x, end=" ")

print('\n')
print("----------------------不可变对象传递------------------------------------------")

def ChangeInt(a):
    a = 10
    print(a,end = "--->a的值 \n")
b = 2
ChangeInt(b)
print(b,end = "--->b的值")


print("\n")
print("----------------------可变对象传递------------------------------------------")

# 可写函数说明
def changeme( mylist ):
   "修改传入的列表"
   mylist.append([1,2,3,4])
   print ("函数内取值: ", mylist)
   return
 
# 调用changeme函数
mylist = [10,20,30]
changeme( mylist )
print ("函数外取值: ", mylist) 

print("\n")
print("----------------------关键字参数------------------------------------------")

#可写函数说明
def printme( str , a, b , c):
   "打印任何传入的字符串"
   print (str+a+b+c)
   return
 
#调用printme函数
printme( str = "菜鸟教程", b = "hehe" , a = "haha", c = "eeee`")


print("\n")
print("----------------------默认参数------------------------------------------")

#可写函数说明
def printinfo( name, age = 35 ): # 默认参数的值 age = 35
   "打印任何传入的字符串"
   print ("名字: ", name)
   print ("年龄: ", age)
   return
 
#调用printinfo函数
printinfo( age=50, name="runoob" )
print ("------------------------")
printinfo( name="runoob" )