#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-14 23:49:36
@file       :day_03_01.Request.quote.py
@software   :PyCharm
"""
# 导入urllib.parse模块
import urllib.parse


base_url = 'https://www.baidu.com/s?wd='
kw = input('清输入：')
# 使用.quote()方法对字符串编码
kw = urllib.parse.quote(kw)
# 拼接url
url = base_url + kw
print(url)

