# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/6/18 下午2:36
# @File     : find_continuous_sequence.py
# Software  : algorithm_study

"""
面试题57 - II. 和为s的连续正数序列
输入一个正整数 target ，输出所有和为 target 的连续正整数序列（至少含有两个数）。
序列内的数字由小到大排列，不同序列按照首个数字从小到大排列。

示例 1：
输入：target = 9
输出：[[2,3,4],[4,5]]

示例 2：
输入：target = 15
输出：[[1,2,3,4,5],[4,5,6],[7,8]]

限制：
1 <= target <= 10^5

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof
"""

"""
题解： 数学 + 枚举
求和为target的 等差为1 的等差数列
则需要求出 等差数量的起始值a1 和等差数量的长度n
求和公式
target = n * a1 + n * (n - 1) / 2
则推到出a1的公式 这里不在多写
然后枚举长度n， 枚举范围起始为2， 最高为 target / 2
然后返回的时候将数组翻转，将n长度小的放在后面
"""


def findContinuousSequence(target: int):
    res = []
    for n in range(2, target // 2):  # 枚举范围 n的起始是2，最大是 target/2
        tmp = target - n * (n - 1) // 2
        if tmp <= 0:
            break
        if not tmp % n:
            a1 = tmp // n
            res.append([a for a in range(a1, a1 + n)])
    return res[::-1]
