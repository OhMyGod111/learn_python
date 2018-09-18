#!/usr/bin/python3


print("------只是普通的打印------")

a = 10
print(a)

a = "哈哈"
print(a)

del a
a = "呵呵"
print(a)

print("------------------------------分割线----------------------------------------->")


def main():
    # print ("main函数被优先调用")
    # print (getName())
    # print (getName1("hehe"))
    pass


def getName():
    return "WangPan"


def getName1(name):
    return name + ": tell me!"


# 可写函数说明
def printinfo(name, age=35):
    "打印任何传入的字符串"
    print("名字: ", name)
    print("年龄: ", age)
    return


# 调用printinfo函数
printinfo(age=50, name="runoob")
printinfo(name="runoob", age=50)
print("--------------------------->")
printinfo(name="runoob")

print("------------------------------分割线----------------------------------------->")


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vartuple)


# 调用printinfo 函数
printinfo(70, 60, 50)

print("------------------------------分割线----------------------------------------->")


def printinfo(arg1, *vartuple):
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    for var in vartuple:
        print(var)
    return


# 调用printinfo 函数
printinfo(10)
printinfo(70, 60, 50)

print("------------------------------分割线----------------------------------------->")


def printinfo(arg1, **vardict):  # **vardict 字典类型
    "打印任何传入的参数"
    print("输出: ")
    print(arg1)
    print(vardict)


# 调用printinfo 函数
printinfo(1, a=2, b=3)

if __name__ == '__main__':
    main()
