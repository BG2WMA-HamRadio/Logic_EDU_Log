#!/usr/bin/env python
# _*_ coding utf-8 _*_

"""
@Author     :BG2WMA
@License    : (C) Copyright 2000-2020, BG2WMA
@time       :2020-06-18 02:03:24
@project    :CSDN_Python_Lesson
@file       :py_stander_lib.py
@software   :PyCharm
"""
from collections import OrderedDict
from random import randint
from time import sleep

"""
和普通字典不同，调用OrderDict()可以创建一个有序的空字典。
在遍历字典的时候，我们知道将以添加的顺序获取键值对。
"""
# 调用OrderedDict()生成一个具有‘名字-呼号’键值对的有序字典
# 并将其按照键入顺序打印。
name_calsign = OrderedDict()

name_calsign['jp'] = 'bd2vaa'
name_calsign['wtg'] = 'bg2wma'
name_calsign['cz'] = 'bg2xma'
name_calsign['lsz'] = 'bh2rcv'
name_calsign['wy'] = 'bh2sjs'
name_calsign['w_y'] = 'bh2wy'
name_calsign['xf'] = 'bg2ues'

print('正在整理...')
sleep(1)
for name, callsign in name_calsign.items():
    print(name.title(), '\t的呼号是： \t', callsign.upper())
# 调用OrderedDict()生成一个具有‘型号-厂商’键值对的有序字典
# 并将其按照键入顺序打印。
modle_brand = OrderedDict()

modle_brand['ft-991a'] = 'yaesu'
modle_brand['id-5100'] = 'icom'
modle_brand['郁金香'] = 'DIY'
modle_brand['坚果_II'] = '锤子'

print('\n正在整理...')
sleep(1)
for modle, brand in modle_brand.items():
    print(modle.upper(), '是由%s生产的'%brand.upper())
print()


"""
创建一个类，用来描述骰子。
默认创建一个6面骰子，并投掷10次
用random模块，产生从1到骰子面数之间的正整数
更改骰子的面数位10，再投10次。
更改骰子的面数位20，在投10次。
"""


# 创建一个Die类
class Die(object):

    # 初始化实例面数属性，默认值为6
    def __init__(self, sides=6):
        self._sides = int(sides)

    # 定义一个投掷骰子的方法，用来模拟投掷骰子。
    def roll_die(self, n):
        for i in range(n):
            # 使用randint方法在1和骰子面数（含）之间生成随机正整数。
            x = randint(1, self._sides)
            print(x, ' ', end='')

    # 创建读取/更改实例骰子面数属性的方法，使用@property装饰器使其以只读属性运作。
    @property
    def sides(self):
        return self._sides

    @sides.setter
    def sides(self, sides):
        if int(sides) > 1:
            self._sides = sides


a = Die()
print('Rolling...')
sleep(1)
a.roll_die(10)
print('\n6 side die roll 10 times over.\n')

a.sides = 10
print('Rolling...')
sleep(1)
a.roll_die(10)
print('\n10 side die roll 10 times over.\n')

a.sides = 20
print('Rolling...')
sleep(1)
a.roll_die(10)
print('\n20 side die roll 10 times over.\n')
