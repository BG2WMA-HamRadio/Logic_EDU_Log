#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-24 17:44:07
@file       :qrz_dxcc.py
@software   :PyCharm
"""
import requests
from lxml import etree
import csv


# 程序功能：从qrz.com/flags网页抓取旗帜连接，DXCC名字， DXCC，以及对应的ISO代码。
# 定义一个获取网页源码的函数，避免频繁访问网站
def get_html():
    url = 'https://www.qrz.com/flags'
    headers = {
        'User-Agent': 'Mozilla / 5.0(Windows NT 10.0;Win64;x64) AppleWebKit / 537.36(KHTML, likeGecko) Chrome / 84.0.4147.89 Safari / 537.36'
    }
    res = requests.get(url, headers=headers)
    html = res.content.decode('utf-8')
    with open('qrz.html', 'w', encoding='utf-8') as fo:
        fo.write(html)


# get_html() 如无特殊需求，运行一次即可。
# 定义函数读取html文件并构建element对象
def build_element():
    with open('qrz.html', 'r') as fi:
        html = fi.read()

    html_element = etree.HTML(html)
    return html_element


# 定义一个字典，存储爬取的数据,并将结果保存到列表中
def save_to_dic(h_element):
    # 创建一个存放字典的列表
    dxcc_list = []
    # 使用xpath方法获取数据：
    flag_urls = h_element.xpath('//td[@class="dp"]/a/img/@src')

    country_names = h_element.xpath('//td/a/text()')
    # 删除冗余数据
    for i in country_names:
        if i == '\n\t    ':
            country_names.remove(i)

    dxccs = h_element.xpath('//td[@class="dc"][1]/text()')

    isos_element = h_element.xpath('//td[@class="dc"][2]')
    # 将空值替换为空格，防止错位
    isos = []
    for iso in isos_element:

        if iso.xpath('text()') == []:
            isos += [' ']
        else:
            isos += iso.xpath('text()')
    # 将每一个DXCC的数据存储到一个字典中，并将得到的字典加入列表。
    for i in range(len(flag_urls)):
        dxcc_dict = {}
        dxcc_dict['flag link'] = flag_urls[i]
        dxcc_dict['Country Name'] = country_names[i]
        dxcc_dict['DXCC'] = dxccs[i]
        dxcc_dict['ISO'] = isos[i]
        dxcc_list.append(dxcc_dict)
    return dxcc_list


# 定义写入csv文件的函数
def write_csv(dxcc_list):
    with open('dxcc.csv', 'w', encoding='utf-8', newline='') as fo:
        # 定义write对象，用来实现csv文件的写入
        write = csv.DictWriter(fo, fieldnames=['flag link', 'Country Name', 'DXCC', 'ISO'])
        # 写入标题行
        write.writeheader()
        # 写入内容行
        for each in dxcc_list:
            write.writerow(each)


if __name__ == '__main__':
    h_element = build_element()
    dxcc_list = save_to_dic(h_element)
    print(dxcc_list)
    write_csv(dxcc_list)
