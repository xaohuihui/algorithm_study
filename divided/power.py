# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2019/12/18 
# @File     : power.py
# Software  : algorithm_study

"""
x**n
"""


# def my_pow(x, n) -> float:
#     if not n:
#         return 1
#     if n < 0:
#         return 1 / my_pow(x, -n)
#     if n % 2:
#         return x * my_pow(x, n - 1)
#     return my_pow(x * x, n / 2)

def my_pow(x, n) -> float:
    if not n:
        return 1
    if n < 0:
        x = 1 / x
        n = -n
    pow_x = 1
    while n:
        if n & 1:
            pow_x *= x
        x *= x
        n >>= 1
    return pow_x


if __name__ == '__main__':
    print(my_pow(2, 10))
