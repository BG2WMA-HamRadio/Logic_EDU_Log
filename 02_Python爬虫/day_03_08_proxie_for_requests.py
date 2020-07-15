#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-16 00:47:15
@file       :day_03_08_proxie_for_requests.py
@software   :PyCharm
"""
import requests
# 定义代理服务器组
proxy = {
    'http': '192.168.1.1:9000'
}
url = 'http://httpbin.org/ip'
# 在requests.get()中添加proxie参数调用代理服务器。
ip = requests.get(url, proxies=proxy).text

print(ip)
