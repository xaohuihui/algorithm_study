# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2019/12/25 
# @File     : fibonacci.py
# Software  : algorithm_study


def fibonacci(n: int) -> list:
    F = [0, 1]
    for i in range(2, n + 1):
        F.append(F[i - 1] + F[i - 2])
    return F[:n + 1]


if __name__ == '__main__':
    res = fibonacci(100)
    print(res)
