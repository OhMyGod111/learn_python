#!/usr/bin/python3
# -*- coding: utf-8 -*-
import re

def main():
    '''
    group(num=0)	匹配的整个表达式的字符串，group() 可以一次输入多个组号，在这种情况下它将返回一个包含那些组所对应值的元组。
    :return:
    '''
    print(re.match('apple', 'apple banana pear').group())
    print(re.match('apple', 'apple banana pear').groups())
    print(re.match('apple', 'apple banana pear').span())
    print(re.match('pear', 'apple banana pear'))

if __name__ == '__main__':
    main()
