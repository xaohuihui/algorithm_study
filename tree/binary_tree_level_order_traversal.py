# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2019/12/19 
# @File     : binary_tree_level_order_traversal.py
# Software  : algorithm_study

"""
102. 二叉树层级遍历
"""

import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


# 广度优先遍历方法
# def level_order(root: TreeNode) -> list:
#     if not root:
#         return []
#
#     queue = collections.deque()  # 申请一个双端队列
#     queue.append(root)
#     result = []
#
#     # visited = set(root)   # 因为是树的结构，所以只要向下走不会存在重复的情况
#
#     while queue:
#         level_size = len(queue)
#         current_level = []
#
#         for _ in range(level_size):
#             node = queue.popleft()  # 这里从左边出了，下面加入的时候就要加到末尾，若是从右边出，则下面从左边push进去
#             current_level.append(node.val)
#
#             if node.left:
#                 queue.append(node.left)
#             if node.right:
#                 queue.append(node.right)
#         result.append(current_level)
#     return result


# 依靠深度优先遍历的算法
def level_order(root: TreeNode) -> list:
    if not root:
        return []

    result = []
    level_size = 0
    result = depth_first_search(root, level_size, result)
    return result


def depth_first_search(root, level, result):
    if not root:
        return []

    if len(result) < level + 1:
        result.append([])

    result[level].append(root.val)
    depth_first_search(root.left, level + 1, result)
    depth_first_search(root.right, level + 1, result)
    return result


if __name__ == '__main__':
    node1 = TreeNode(1)
    node2 = TreeNode(2)
    node3 = TreeNode(3)
    node4 = TreeNode(4)
    node5 = TreeNode(5)
    node6 = TreeNode(6)
    node7 = TreeNode(7)

    node4.left = node2
    node2.left = node1
    node2.right = node3
    node4.right = node6
    node6.left = node5
    node6.right = node7
    print(level_order(node4))
