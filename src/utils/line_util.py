#!/usr/bin/python3

def cuttingLine(describe):
    print("\n")
    print("---------------------" + describe + "------------------------------>>>")


# 斐波那契(fibonacci)数列模块
def fib(n):  # 定义到 n 的斐波那契数列
    a, b = 0, 1
    while b < n:
        print(b, end=' ')
        a, b = b, a + b
    print()


def fib2(n):  # 返回到 n 的斐波那契数列
    result = []
    a, b = 0, 1
    while b < n:
        result.append(b)
        a, b = b, a + b
    return result


if __name__ == '__main__':
    # main()
    # print("程序自身在运行")
    pass
else:
    # print("我来自另一模块")
    pass
