#!/usr/bin/python3

a  = "HelloWord!"

print(a[0])
print(a[1:5])
print(a*2 + "// 字符串重复")

print('W' in a) # "// 成员运算符"
print("W" not in a) # "// 成员运算符"

b = "hehehehehehe \n hehehehehehe"
print(b)
c = r"hehehehehehe \n hehehehehehe"
print(R"hehehehehehe \n hehehehehehe")
print(c)

print("\n")
print("\n")
print("\n")

print("--------------------------字符串格式化------------------------------")

d = "我叫 %s 今年 %d 岁!" % ('小明', 10)
print (d)

def getMe(name,age):
	return "我叫 %s 今年 %d 岁!" % (name, age)

print(getMe("王尼玛",20))