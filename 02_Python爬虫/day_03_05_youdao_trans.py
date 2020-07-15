#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-15 15:12:11
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_05_youdao_trans.py
@software   :PyCharm
"""
import urllib.parse
import urllib.request
import random
import json
"""
制作一个有道翻译软件
"""
key_word = input('请输入要翻译的内容： ')
# url地址要将‘_o’删除
url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {}
path = './UA/'
f_l = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
u_f = random.choice(f_l)
full_file = path + u_f
with open(full_file, 'r') as fi:
    uas = fi.readlines()
    ua = random.choice(uas).strip()
headers['User-Agent'] = ua

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
# 对字典编码并转换为字节流。
data = urllib.parse.urlencode(data)
data =bytes(data, 'utf-8')
# 生成请求
req = urllib.request.Request(url, data=data, headers=headers)
# 获取相应
res = urllib.request.urlopen(req)
# 读取响应
html = res.read().decode('utf-8')
# 将结果解构成答案
ans = json.loads(html)
answer = ans['translateResult'][0][0]['tgt']

print(answer)
