#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-07-15 09:41:31
@project    :CSDN_Python_Lesson_scrapy
@file       :day_03_04_exerice_tieba_with_class.py
@software   :PyCharm
"""
# 导入模块
import urllib.parse
import urllib.request
import random

"""
仍然是爬取贴吧，这个程序使用类来完成
创建类
在类中定义获取网站内容和写入文件的方法
"""


# 创建一个没有父类的类
class Tieba:
    """
    爬取百度贴吧的类
    """

    def __init__(self):
        """
        定义一个init函数，存放不可改变的参数，并赋予初始值。
        """
        self.headers = {}
        self.base_url = 'https://tieba.baidu.com/f?'

    def get_ua(self):
        """
        从UA文件夹中随机选取文件，并从被选择的文件中随机抽取一个UA
        :return: ua --> str
        """
        path = './UA/'
        file_list = ['Chrome.txt', 'Edge.txt', 'Firefox.txt', 'Mozilla.txt', 'Opera.txt', 'Safari.txt']
        # 选择一个文件
        full_fn = path + random.choice(file_list)
        # 在文件中抽取一个UA
        with open(full_fn, 'r') as ua_fi:
            ua_list = ua_fi.readlines()
            ua = random.choice(ua_list).strip()
            return ua

    def read_page(self, url):
        # 重构 User-Agent
        ua = self.get_ua()
        self.headers['User-Agent'] = ua
        # 发起请求
        req = urllib.request.Request(url, headers=self.headers)
        # 获取响应
        res = urllib.request.urlopen(req)
        # 读取页面
        html = res.read().decode('utf-8')
        return html

    def write_file(self, file_name, html):
        """
        按照指定的文件名，将html的内容写入文件。
        :param file_name: 由用户或者程序指定的文件名 --> str
        :param html: 调用read_url函数获得的html内容 --> str
        :return: None
        """
        with open(file_name, 'w', encoding='utf-8') as fo:
            fo.write(html)
            print('正在写入文件...')

    def main(self):
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
            url = self.base_url + kw + '&pn=' + str((i - 1) * 50)
            # 调用读取内容函数，爬取网页内容。
            html = self.read_page(url)
            # 调用写入文件函数，将读取的内容写入文件。
            self.write_file(file_name, html)


if __name__ == '__main__':
    spider = Tieba()
    spider.main()
