#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-15 02:16:18
@file       :day_03_03_exerice_tieba_with_func.py
@software   :PyCharm
"""
# 导入需要的模块：
import urllib.parse
import urllib.request
import os
import random

"""
还是爬取贴吧的内容
用函数的方式进行
需要的函数：
获取user-agent的函数
访问网络并返回内容的函数
写入文件的函数
主函数： main

"""


# 定义获取user-agent的函数
def get_UA():
    """
    随机打开txt文件中，并在文件中随机选取UA
    :return: 不同浏览器，不同版本，不同操作系统的UA --> str
    """
    # 根据具体操作系统和文件位置定义下列变量，经测试，这段代码可以在windows 10和linux上正常运行。
    path = './UA/'
    file_list = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
    # 随机选取一个文件作为获得UA的主文件
    use_file = random.choice(file_list)
    full_path = path + use_file
    # 在主文件中随机选取一个ua返回给程序调用。
    with open(full_path, 'r') as f_u:
        agents = f_u.readlines()
        res = random.choice(agents).strip()
        return res


def read_url(url):
    """
    读取指定url的地址，并将结果返回给程序调用。
    :param url: 一个已经完成编码的完整的url
    :return: 读取到的完整的html文件 --> str
    """
    # 给headers定义一个空的字典
    headers = {}
    # 调用函数，随机获取一个U-A，防止服务器Ban IP.
    user_agent = get_UA()
    # 将 U-A 加入 headers
    headers['User-Agent'] = user_agent
    # 发起请求
    req = urllib.request.Request(url, headers=headers)
    # 获取相应
    res = urllib.request.urlopen(req)
    # 读取页面
    html = res.read().decode('utf-8')
    # 返回结果
    return html


def write_file(file_name, html):
    """
    按照指定的文件名，将html的内容写入文件。
    :param file_name: 由用户或者程序指定的文件名 --> str
    :param html: 调用read_url函数获得的html内容 --> str
    :return: None
    """
    with open(file_name, 'w', encoding='utf-8') as fo:
        fo.write(html)
        print('正在写入文件...')


def main():
    # 爬取网页所需要的基础数据
    base_url = 'https://tieba.baidu.com/f?'
    # 对 关键字编码
    k_w = input('请输入需要爬取的关键字：')
    kw = {'kw': k_w}
    kw = urllib.parse.urlencode(kw)
    # 获取起止页面
    start_page = int(input('请输入起始页：'))
    end_page = int(input('请输入结束页：'))

    for i in range(start_page, end_page + 1):
        # 定义写入的文件名
        file_name = k_w + '.' + str(i) + '.html'
        # 拼接URL
        url = base_url + kw + '&pn=' + str((i - 1) * 50)
        # 调用读取内容函数，爬取网页内容。
        html = read_url(url)
        # 调用写入文件函数，将读取的内容写入文件。
        write_file(file_name, html)


if __name__ == '__main__':
    main()
