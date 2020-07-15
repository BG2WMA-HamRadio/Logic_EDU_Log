#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-16 00:36:33
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_07_func_of_requests.py
@software   :PyCharm
"""
# 导入requests模块
import requests
import json
import random
"""
requests模块中的post请求
可以自动对请求头和参数进行编码
"""

# 构建请求头中的UA
headers = {}
path = './UA/'
f_l = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
u_f = random.choice(f_l)
full_file = path + u_f
with open(full_file, 'r') as fi:
    uas = fi.readlines()
    ua = random.choice(uas).strip()
# 重构请求头
headers['User-Agent'] = ua
# 定义post所需的参数
key_word = input('请输入需要翻译的内容：')
data ={
    'i': key_word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '15947970677615',
    'sign': '7e7f783d713bc54a1b8216a937f8e53d',
    'ts': '1594797067761',
    'bv': '02a6ad4308a3443b3732d855273259bf',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_REALTlME'
}

url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
# 发起请求，并获取响应
res = requests.post(url, data=data, headers=headers)
# 对相应结果解码。
html = res.content.decode('utf-8')

resoult = json.loads(html)

answer = resoult['translateResult'][0][0]['tgt']

print(answer)


