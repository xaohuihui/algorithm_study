# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/1/15 
# @File     : bit_operation.py
# Software  : algorithm_study

"""
位运算
"""


# No.1
# def number_of_1(n):
#     count = 0
#     # 先转化为正的
#     if n < 0:
#         n = n & 0xffffffff  # 2 ** 32
#
#     while n:
#         if n & 1:
#             count += 1
#         n = n >> 1
#     return count


# No.2
def number_of_1(n):
    count = 0
    # 先转化为正的
    if n < 0:
        n = n & 0xffffffff  # 2 ** 32
    while n:
        count += 1
        n = (n - 1) & n
    return count


if __name__ == '__main__':
    args = -(2 ** 31)  # 2 ** 32

    print(number_of_1(args))
