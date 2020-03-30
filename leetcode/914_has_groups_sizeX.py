# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/3/27 下午4:57
# @File     : 914_has_groups_sizeX.py
# Software  : algorithm_study

"""914. 卡牌分组"""

"""
fractions.gcd(a, b)返回两个值的最大公约数 3.5 版后已移除: 由 math.gcd() 取代.
"""


def has_groups_size_x(deck):
    from math import gcd
    from collections import Counter
    from functools import reduce
    vals = Counter(deck).values()
    return reduce(gcd, vals) >= 2


if __name__ == '__main__':
    print(has_groups_size_x([1, 2, 3, 4, 4, 3, 2, 1]))
