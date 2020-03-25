# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/3/25 下午2:57
# @File     : test.py
# Software  : algorithm_study

"""
892. 三维形体的表面积
"""


def surface_area(grid):
    area = 0
    n = len(grid)
    for i in range(n):
        for j in range(n):
            area += grid[i][j] * 4 + 2 if grid[i][j] else 0
            if j > 0:
                area -= min(grid[i][j - 1], grid[i][j]) * 2
                area -= min(grid[j - 1][i], grid[j][i]) * 2
    return area


if __name__ == '__main__':
    print(surface_area([[1, 0], [0, 2]]))
