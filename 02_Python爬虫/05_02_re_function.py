#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-19 13:35:05
@file       :day_05_02_re_exec_continue.py
@software   :PyCharm
"""
# 依然是主要练习re模块的使用。
# 导入 re 模块
import re

# 定义函数，打开上节内容获取的数据文件，读取数据文件内容
def read_file():
    with open('qrz.html', 'r', encoding='utf-8') as fi:
        html = fi.read()
    return html
# 调用函数，获取内容。
# html = read_file()

# 定义函数来执行ptn，并返回结果
def re_ptn(ptn, lst):
    for x in lst:
        res = re.match(ptn, x)
        if res:
            print(x, '匹配成功，匹配结果是：', res.group())
        else:
            print(x, '匹配失败')
# re模块的三大查找方法：match, search, findall

# 查找所有id，id为全数字 --> List
# 位于 <tr class="lrow" data-rownum="529810338" style="background-color: #DFD; x"> 中的数字
# ids = re.findall(r'<tr class="lrow" data-rownum="(\d+)" style="background-color: #DFD; x">', html, re.S)
# # 查找所有呼号 --> List
# # 呼号中有数字也有字母
# cSs = re.findall(r'<td class="lde".*?>(.*?)</td>', html, re.S)
# # 查找所有姓名： --> List
# # 姓名中通常不含有字母
# names = re.findall(r'<td class="lcc" style=.*?>(.*?)</td>', html, re.S)

# print(ids, len(ids))
# print(cSs, len(cSs))
# print(names, len(names))

# re 功能的实现
# . 匹配除了换行符外的任意字符
# \w 匹配 a-z、A-Z、0-9、‘_' 下划线, \W是反集
# \d 匹配数字， \D匹配非数字。
# 匹配以2个字母开头的呼号
# {m}, 匹配前一个字符m次，{m, n}, 匹配前一个字符至少m次，最多n次， {m, }匹配前一个字符，无上限。
ptn = '\w{2}.'    # 匹配成功，匹配结果是： VK2 ... 所有结果都是3位
ptn = '\d{2, 9}'    # 显示全部9位数字，如果前边{2, 8}则只显示前8位。
ptn = '\d{1, }'     # 一直显示至不是数字为止
# re_ptn(ptn, cSs)

# + 匹配前一个字符，一次或者多次（最少一次）
# 匹配以一个字符开头，第二位是数字，显示整个呼号
ptn = '\w\d.+'    # 匹配成功，匹配结果是： K6BRN 给出所有符合要求的呼号
# re_ptn(ptn, cSs)

# [] 匹配字符集中列举的字符
# \d 匹配数字
# | 逻辑或
ptn = '5[2|3]\d+'
# re_ptn(ptn, ids)

# \s 匹配空白， \S是反集
ptn = '\w+\s\w+'

# * 匹配前一个字符0次至无限次， 亦即可有可无

ptn = '\w*'        # 匹配至出现空客
ptn = '\w.*'       # 匹配非空字符串，显示所有字符

# 匹配邮箱，电话号，网址的re规则，到处都是，自己google一下吧。

# re_ptn(ptn, names)

# 方法的介绍
# compile() 根据包含正则表达式的字符串创建模式对象。
# 把正则表达式的模板转换为对象。好处是有些时候效率较高。
# 例创建一个匹配字符abc的对象
pnt = re.compile(r'abc')
s = pnt.match('abcde').group()
# print(s)           # abc

# flag 匹配模式：
# re.S，匹配换黄的数据。 re.I：大小写不敏感， re.A: ASCII字符
pnt1 = re.compile(r'ABC', re.I)
s1 = pnt1.match('abcdefg').group()
# print(s1)

# search() 在文本内查找，返回第一个匹配的字符串
# 与match() 的区别是查找的文职不用固定在文本的开头。
res = re.search(r'abc', '123abc456abc789').group()
# print(res)             # abc

# findall() 与match()和search的区别是，前两者都是单值匹配。
# findall() 方法将匹配到的数据返回一个列表
res1 = re.findall(r'abc', '123abc456abc789')  # 不要加group
# print(res1)                #   ['abc', 'abc']

# split(), 和字符串中的split相似
# 不同的是，re.split()可以使用正则表达式作为参数。
# split() 方法有max参数，将字符串分割为max +1段，顺序输出为列表项
s = '8 + 7 * 6 / 3'
s1 = re.split(r'[\+\-\*\/]', s)              # + * 有特殊含义，添加转移字符
# print(s1)

# sub(), 替换。 类似于replace， 根据正则表达式将字符串中的匹配字符替换为sub方法指定的字符串
s = "the people's republic of china"
s1 = re.sub(r'e', 'E', s)          # 参数为止： 要被替换的字符， 替换的字符， 需要被替换的字符串。
# print(s1)

# 分组功能
# re模块有一个分组功能，将已经匹配到的内容，再筛选出需要的内容
# 获取分组内容需要使用group() 和 groups()
# 分组功能通过 "()"实现
text = 'apple price is $99, orange price is $88'
# 需求： 找到$99 和 $88
# 使用search()方法

# res = re.search('.+(\$\d+).+(\$\d+)', text)
# print(res.group())              # apple price is $99, orange price is $88 匹配整个分组
# print(res.group(0))             # apple price is $99, orange price is $88 匹配整个分组
# print(res.group(1))             # $99    匹配第一个分组
# print(res.group(2))             # $88    匹配第二个分组... 以此类推
# print(res.groups())             # ('$99', '$88')    # 获取所有分组，返回得到的元组。

# 使用 findall()分组的方法
res1 = re.findall(r'\$\d+', text)
print(res1)
