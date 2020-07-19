#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-18 19:54:21
@file       :day_05_re_execire.py
@software   :PyCharm
"""
import re
import requests
import json
# 本代码只是用来练习为练习re模块提供数据，并不能实际爬取log。实习操作需要使用etree。
# 正确的思路是将每一条Log的所有信息集中存储到一个条目中（字典的key-value, 数据库的单独记录，或者电子表格的一行）

url = 'https://logbook.qrz.com/'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36',
    'Referer': 'https://www.qrz.com/',
    # Cookie在此省略
    'Cookie': 'xxx; yyy; zzz'
}
# 为避免多次请求，将爬取代码写作函数形式，需要时调用。
def get_date():
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    f_name = 'qrz.html'
    with open(f_name, 'w', encoding='utf-8') as fo:
        fo.write(html)

# get_date()
# 将获得的文件打开并进行分析。
with open('qrz.html', 'r') as fi:
    f = fi.read()
    # print(f)
# 提取所有呼号
# <td class="lde" style="" onclick="lbshow(2, 530743266);">BG5CNL</td>
call_sign = []
c_sign = re.findall(r'<td class="lde" .*?>(.*?)</td>', f, re.S)
for cs in c_sign:
    # 将‘&#216；’替换为字符’0‘
    call_sign.append(re.sub(r'&#216;', '0', cs))
# print(call_sign, len(call_sign))

# 提取国家
# <td class="lcc" onclick="lbshow(0, 530791150);">Australia</td>
country = []
c_country = re.findall(r'<td class="lcc" onclick=.*?>(.*?)</td>', f, re.S)
# print(c_country, len(c_country))

# 提取姓名
# <td class="lcc" style="color: #00a;" onclick="lbshow(0, 530791150);">John Harris</td>
name_list = []
name = re.findall(r'<td class="lcc" style.*?>(.*?)</td>', f, re.S)
# print(name, len(name))

# 将得到的数据打包
# 此处应进一步练习将所得到的数据写入json和Excel的方法。

cs_list = []
for i in range(100):
    c = {}
    c['CallSign'] = call_sign[i]
    c['Country'] = c_country[i]
    c['Name'] = name[i]
    cs_list.append(c)
# print(cs_list)
# 写入json数据
c_json = json.dumps(cs_list)
print(c_json)
# 写入json文件， 为避免重复写入文件，此处将写入json文件定义为函数。
def write_json():
    js_file = 'cs.json'
    with open(js_file, 'w') as fo:
        json.dump(cs_list, fo)
