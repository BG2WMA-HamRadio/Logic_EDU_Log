#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-16 00:11:58
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_06_requests.py
@software   :PyCharm
"""
# 导入requests模块
import requests
import random

headers = {}
path = './UA/'
f_l = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
u_f = random.choice(f_l)
full_file = path + u_f
with open(full_file, 'r') as fi:
    uas = fi.readlines()
    ua = random.choice(uas).strip()
headers['User-Agent'] = ua
wd = {'wd': 'python'}
# 发起请求
# param: 参数， params: 多个参数
res = requests.get('https://www.baidu.com/s?', params=wd, headers=headers)

# 获取响应对象
print(res)    #  <Response [200]> 获得对象

# 获得响应内容 --> str 响应结果是字符类型的，使用text，不可以使用res.text.decode()
# res.text属性（方法@properties）已经将content进行了自动解码，不能再次解码。
# res.text自动对res.content进行解码，自动选择的解码方式如果发生错误，就会出现乱码现象。
# 这种情况需要通过 res.content.decode('编码方式')强制解码。
txt = res.text
# 也可以用下面的方法解码： res.encoding = 'utf-8'

con = res.content                    # 获得响应内容 --> bytes
con_decode = con.decode('utf-8')     # 对字节流数据解码。数据是图片/音乐/音频等，使用content
uRl = res.url                        # 返回请求的url
# print(txt)
# print(con)

# 处理不信任的SSL(安全套接层)证书
# 在requests.get的参数中添加verify=False
url = 'http://www.china.com'
res = requests.get(url, verify=False)
