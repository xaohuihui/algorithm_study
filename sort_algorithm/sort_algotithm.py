# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 20-1-14 上午10:14
# @File     : sort_algotithm.py
# Software  : algorithm_study


def bubble_sort(arr: list) -> list:
    """
    冒泡排序
    :param arr:
    :return:
    """
    for i in range(1, len(arr)):
        for j in range(len(arr) - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def select_sort(arr: list) -> list:
    """
    选择排序
    :param arr:
    :return:
    """
    for i in range(len(arr) - 1):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j

        if min_index != i:
            arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


def insert_sort(arr: list) -> list:
    """
    插入排序
    :param arr:
    :return:
    """
    for i in range(len(arr)):
        pre_index = i - 1
        current = arr[i]
        while pre_index >= 0 and arr[pre_index] > current:
            arr[pre_index + 1] = arr[pre_index]
            pre_index -= 1
        arr[pre_index + 1] = current
    return arr


def shell_sort(arr: list) -> list:
    """
    希尔排序
    :param arr:
    :return:
    """
    length = len(arr)
    gap = length // 2  # 初始步长
    while gap > 0:
        for i in range(gap, length):
            # 每个步长进行插入排序
            temp = arr[i]
            j = i - gap
            # 插入排序
            while j >= 0 and arr[j] > temp:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
        # 得到新的步长
        gap = gap // 2
    return arr


"""
归并排序
采用分治方法
分为左右两个列表，将左边分到最小力度,进行排序
"""


def merge_sort(arr):
    length = len(arr)
    if length < 2:
        return arr
    middle = length // 2
    left, right = arr[0:middle], arr[middle:]
    print(left, right)
    return merge(merge_sort(left), merge_sort(right))


def merge(left, right):
    print("left, right", left, right)
    result = []
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    print("result", result)
    return result


if __name__ == '__main__':
    arr_a = [12, 8, 52, 0, 29, 7, 5, 4, 3]
    # print(bubble_sort(arr_a))
    # print(select_sort(arr_a))
    # print(insert_sort(arr_a))
    # print(shell_sort(arr_a))
    print(merge_sort(arr_a))
