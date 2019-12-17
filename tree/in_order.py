# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 2019/12/16 下午7:20
# @File     : in_order.py
# Software  : algorithm_study

"""
中序遍历
"""


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def in_order(root: TreeNode) -> list:
    if root is None:
        return []
    return in_order(root.left) + [root.val] + in_order(root.right)


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

    print(in_order(node4))
