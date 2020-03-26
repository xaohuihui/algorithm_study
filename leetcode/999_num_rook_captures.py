# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2020/3/26 上午10:58
# @File     : 999_num_rook_captures.py
# Software  : algorithm_study

"""999. 车的可用捕获量"""


def num_rook_rook_captures(board):
    num = 0
    r_site = []
    for i in range(8):
        for j in range(8):
            if board[i][j] == 'R':
                r_site = [i, j]
                break
    if r_site:
        for x, y in [[0, 1], [0, -1], [1, 0], [-1, 0]]:  # 右，左，下，上
            x_site = r_site[0] + x
            y_site = r_site[1] + y
            while 0 <= x_site < 8 and 0 <= y_site < 8:
                if board[x_site][y_site] == 'p':
                    num += 1
                    break
                if board[x_site][y_site] == 'B':
                    break
                x_site += x    # 这里恒定向一个方向走
                y_site += y

    return num


if __name__ == '__main__':
    b = [[".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", "R", ".", ".", ".", "p"], [".", ".", ".", ".", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", "p", ".", ".", ".", "."],
         [".", ".", ".", ".", ".", ".", ".", "."], [".", ".", ".", ".", ".", ".", ".", "."]]

    print(num_rook_rook_captures(b))
