# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/3/30 上午10:56
# @File     : 62_last_remaining.py
# Software  : algorithm_study

"""62. 圆圈中最后剩下的数字"""


def last_remaining(n: int, m: int) -> int:
    n_list = [item for item in range(n)]
    flag = 0
    length = len(n_list)
    while length > 1:
        flag = flag + m
        while flag > length:  # 若超出n_list长度，从头记起
            flag = flag - length
        n_list.pop(flag - 1)
        length -= 1
        flag -= 1
    return n_list[0]


def last_remaining_2(n: int, m: int) -> int:
    res = 0
    for i in range(2, n + 1):
        print(res, '!!!!!!!!!!!!!!!!', i)
        res = (res + m) % i
    return res


if __name__ == '__main__':
    print(last_remaining(10, 17))
    print(last_remaining_2(10, 17))
