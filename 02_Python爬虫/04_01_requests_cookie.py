#!/usr/bin/env python
# _*_ coding utf-8 _*_
# 使用cookie和POST方法，爬取QRZ.COM的Loogbook页
"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-17 01:32:18
@file       :day_04_requests_cookie.py
@software   :PyCharm
"""
import requests
import random

# 定义URL, Headers, data, UA...
url = 'https://logbook.qrz.com/logbook'
path = '../UA/'
f_l = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
u_f = random.choice(f_l)
full_file = path + u_f
with open(full_file, 'r') as fi:
    uas = fi.readlines()
    ua = random.choice(uas).strip()
# POST请求所需的data，此处省略
data = {
   'xxx': 'yyy'
   .
   .
   .
}
# 重构headers
headers = {
        'User-Agent': ua,
    # Cookies 用来获得登录网站后的页面。此处省略。
        'Cookie': 'xxx; yyy; zzz',
    # Referer 来源网站，防止反爬
        'Referer': 'https://logbook.qrz.com/logbook'
}
# 发起请求并获取结果。
res = requests.post(url, data=data, headers=headers)
html = res.content.decode('utf-8')
file_name = 'p1.html'
# 将得到的html保存至文件。
with open(file_name, 'w', encoding='utf-8') as fo:
    fo.write(html)
