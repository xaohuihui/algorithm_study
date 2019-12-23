# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-23 下午2:43
# @File     : two_sum.py
# Software  : algorithm_study

"""
两数之和
"""


def two_sum(nums: list, target: int) -> list:
    _dict = {}
    for i, m in enumerate(nums):
        if _dict.get(target - m) is not None:
            return [i, _dict[target - m]]
        _dict[m] = i


if __name__ == '__main__':
    nums_list = [1, 3, 4, 5, 6, -1, 2]
    print(two_sum(nums_list, 11))
