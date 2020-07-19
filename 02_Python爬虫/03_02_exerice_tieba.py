#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-15 00:59:20
@file       :day_03_02_exerice_tieba.py
@software   :PyCharm
"""

"""
练习内容：
1. 输入要爬取贴吧的主题。
2. 输入爬取的起始页和终止页。
3. 把每一页的内容爬取保存到本地

对程序的分析：
1，分析百度贴吧的地址，并分析变化：
    - https://tieba.baidu.com/f?kw=%E4%B8%9A%E4%BD%99%E6%97%A0%E7%BA%BF%E7%94%B5&ie=utf-8&pn=50
    - url中的‘&ie=utf-8’可以省略。
    - pn = (当前页面数 - 1) * 50
    - kw = 要爬取的关键字
2. 重构请求头
    - 引用random模块
    - 利用u_agent.py文件存储的多个User-Agent
    - 利用random.choice()方法从多个User-Agent文件中随机选取一个UA
3. 使用input()函数获取需要爬取贴吧的关键字
4. 使用urllib.parse.urlencode()函数构建kw
5. 使用urlib.request.Request()函数生成并返回对象
6. 使用urllib.request.open()函数访问并返回网站
7. 使用read().decode('编码')获取网页内容
8. 使用 with open() as讲结果保存到文件。

"""
# 导入所需的函数：
import urllib.request
import urllib.parse
import random
import os

# 定义基础url
base_url = 'https://tieba.baidu.com/f?'
# 重构请求头：
# 从UA文件夹中随机选取UA文件，并从文件中随机选取一条User-Agent
headers = {}
path = './UA/'
f_l = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
u_f = random.choice(f_l)
full_file = path + u_f
with open(full_file, 'r') as fi:
    uas = fi.readlines()
    ua = random.choice(uas).strip()
    headers['User-Agent'] = ua

# 定义变量
k_w = input('输入需要爬取的关键字：')
kw = {'kw': k_w}
kw = urllib.parse.urlencode(kw)

start_page = int(input('输入起始页'))
end_page = int(input('输入结束页：'))

for i in range(start_page, end_page + 1):
    url = base_url + kw + '&pn=' + str((i - 1) * 50)
    req = urllib.request.Request(url)
    res = urllib.request.urlopen(req)
    html = res.read().decode('utf-8')
    file_name = k_w + '.' + str(i) + '.html'
    with open(file_name, 'w', encoding='utf-8') as f:
        f.write(html)
        print('正在写入...')
