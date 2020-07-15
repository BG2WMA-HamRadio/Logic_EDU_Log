#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-14 23:49:36
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_01.Request.quote.py
@software   :PyCharm
"""
import urllib.parse

base_url = 'https://www.baidu.com/s?wd='
kw = input('清输入：')
kw = urllib.parse.quote(kw)
url = base_url + kw
print(url)

