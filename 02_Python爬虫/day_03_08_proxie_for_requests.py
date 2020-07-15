#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-16 00:47:15
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_08_proxie_for_requests.py
@software   :PyCharm
"""
import requests

proxy = {
    'http': '192.168.1.1:9000'
}
url = 'http://httpbin.org/ip'
ip = requests.get(url, proxies=proxy).text

print(ip)
