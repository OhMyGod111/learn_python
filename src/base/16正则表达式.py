#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import re

from src.utils import line

"""
    \d 匹配一个数字
    \D 匹配任意非数字
    \w 匹配一个字母或数字
    \s 匹配一个空格（也包括Tab等空白符），所以\s+表示至少有一个空格，例如匹配' '，' '等；
    .  匹配任意字符  例如：'py.'可以匹配'pyc'、'pyo'、'py!'等等。
    
    用*表示任意个字符（包括0个）
    用+表示至少一个字符
    用?表示0个或1个字符
    用{n}表示n个字符
    用{n,m}表示n-m个字符  例如：\d{3,8}表示3-8个数字，例如'1234567'。
    
    A|B可以匹配A或B，所以(P|p)ython可以匹配'Python'或者'python'。
    ^表示行的开头，^\d表示必须以数字开头。
    $表示行的结束，\d$表示必须以数字结束。
    
    '-'是特殊字符，在正则表达式中，要用‘\’转义
    
    要做更精确地匹配，可以用[]表示范围 
        例如：[a-zA-Z\_][0-9a-zA-Z\_]*   可以匹配由字母或下划线开头，后接任意个由一个数字、
    字母或者下划线组成的字符串，也就是Python合法的变量；
    
"""
def main():
    str1 = '\\hangzhou'   # 由于Python的字符串本身也用\转义
    print(str1)

    '''
    判断正则表达式是否匹配 match
    '''
    obj = re.match(r'^\d{3}\-\d{3,8}$', '010-12456')
    if obj is None:
        print('sorry,没找到与之匹配的结果')
    else:
        print('yes，找到了与之匹配的结果')

    '''
    切分字符串 split
    '''
    # 普通字符串切分
    print('a b c cc dd ss'.split(' '))
    print('a b c cc dd  ss'.split(' ')) # 不能识别多余的加空格
    print('a b c cc dd;  ss'.split(' ')) # 不能识别多余的加空格 特殊符号;
    print('a-b-c-d-e-hello'.split('-'))

    line.line()

    # 使用正则表达式
    print(re.split(r'\s+', 'a b cc dd ee      rr')) # 可以识别多余的空格
    print(re.split(r'[\s\,]+','a,b,c,d,e f  g,,,fd d')) # 无论多少个空格 ,号 ;号都可以识别

    line.line('groups')

    '''
    分组 groups
    正则表达式还有提取子串的强大功能。用()表示的就是要提取的分组（Group）
    '''
    m = re.match(r'^(\d{3})-(\d{3,8})', '012-10086')
    print(m.span())
    print(m.start())
    print(m.end())
    print(m.group(0,1,2))  # 返回元组
    print(m.groups())

    line.line('search ----->')
    m = re.search(r'(abc)', 'pppabc123456abc')
    print(m.span())
    print(m.start())
    print(m.end())
    print(m.group(0,1))  # 返回元组
    print(m.groups())

    t = '19:05:30'
    # 这个正则表达式可以直接识别合法的时间
    m = re.match(r'^(0[0-9]|1[0-9]|2[0-3]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]'
                 r'|5[0-9]|[0-9])\:(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$', t)
    if m :
        print(m.groups())
    else:
        print('时间不合法！')

    line.line('贪婪匹配')
    '''
    贪婪匹配
    '''
    print(re.match(r'^(\d+)(0*)$', '108600').groups())  # \d+采用贪婪匹配
    print(re.match(r'^(\d+?)(0*)$', '108600').groups()) # \d+?采用非贪婪匹配

    line.line('compile')

    '''
    编译  compile
    
    当我们在Python中使用正则表达式时，re模块内部会干两件事情：

        1.编译正则表达式，如果正则表达式的字符串本身不合法，会报错；

        2.用编译后的正则表达式去匹配字符串。
        
    如果一个正则表达式要重复使用几千次，出于效率的考虑，我们可以预编译该正则表达式  
    接下来重复使用时就不需要编译这个步骤了，直接匹配  
    '''
    re_telephone = re.compile(r'^(\d{3})-(\d{3,8})$')

    print(re_telephone.match('010-12345').groups())
    print(re_telephone.match('010-8086').groups())

    line.line('search方法')
    '''
    search方法
    '''
    print(re.search('www', 'www.baidu.com').span())  # 在起始位置匹配
    print(re.search('com', 'www.baidu.com').span())  # 不在起始位置匹配

    line.line("match和search的区别")

    ret_match = re.match("c", "abcde");  # 从字符串开头匹配，匹配到返回match的对象，匹配不到返回None
    if (ret_match):
        print("ret_match:" + ret_match.group());
    else:
        print("ret_match:None");

    ret_search = re.search("c", "abcde");  # 扫描整个字符串返回第一个匹配到的元素并结束，匹配不到返回None
    if (ret_search):
        print("ret_search:" + ret_search.group());

    line.line('检索和替换')
    '''
    检索和替换 sub 用于替换字符串中的匹配项。
    '''
    phone = "2004-959-559 # 这是一个电话号码"
    print(re.sub(r'#.*$', '', phone))  # 删除了注释之后的内容
    print(re.sub(r'\D', '', phone))    # 删除非数字的内容

    # 将匹配的数字乘于 2
    def double(matched):
        value = int(matched.group('value'))
        return str(value * 2)

    s = 'A23G4HFD567'
    print(re.sub('(?P<value>\d+)', double, s))

    line.line("subn")

    print(re.subn('[1-2]', 'A', '123456abcdef'))
    print(re.sub("g.t", "have", 'I get A,  I got B ,I gut C'))
    print(re.subn("g.t", "have", 'I get A,  I got B ,I gut C'))

    line.line('findall')

    """
    findall 匹配的所有子串，并返回一个列表，如果没有找到匹配的，则返回空列表
    """
    pattern = re.compile(r'\d+')   # 查找数字
    result1 = pattern.findall('shanghai 123 beijing 456')
    result2 = pattern.findall('aaa333bbb555ccc666', 0, 18)

    print(result1)
    print(result2)

    line.line('finditer')

    """
    finditer  和 findall 类似，在字符串中找到正则表达式所匹配的所有子串，并把它们作为一个迭代器返回。
    """
    it = re.finditer(r"\d+", "12a32bc43jf3")
    for match in it:
        print(match.group())

    # <editor-fold desc="示例  match 和 search">
    line.line()
    print(re.match('([\w]*)([\d]*)', 'abc123qwe'))
    print(re.match('([\w]*)([\d]*)', 'abc123qwe').group(0,1,2))



    a = "123abc456"
    print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).group(0,1,2,3))  # 123abc456,返回整体
    print(re.search("([0-9]*)([a-z]*)([0-9]*)", a).groups(0))  # 123abc456,返回整体
    # </editor-fold>

    pass


if __name__ == '__main__':
    main()
