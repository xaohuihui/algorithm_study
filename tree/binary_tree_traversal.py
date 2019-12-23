# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-19 上午9:59
# @File     : binary_tree_traversal.py
# Software  : algorithm_study

"""
二叉树遍历，pre_order(先序遍历)、in_order(中序遍历)、post_order(后续遍历)、breadth_first_search(广度优先遍历)、depth_first_search(深度优先遍历)
"""

import collections


class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = self.right = None


def pre_order(root: TreeNode) -> list:
    if not root:
        return []

    return [root.val] + pre_order(root.left) + pre_order(root.right)


def in_order(root: TreeNode) -> list:
    if not root:
        return []

    return in_order(root.left) + [root.val] + in_order(root.right)


def post_order(root: TreeNode) -> list:
    if not root:
        return []

    return post_order(root.left) + post_order(root.right) + [root.val]


def breadth_first_search(root: TreeNode) -> list:
    """
    这个只是二叉树的广度优先遍历，和图的广度优先不同，返回二叉树的遍历顺序
    :param root: TreeNode
    :return: list
    """

    if not root:
        return []

    queue = collections.deque()  # 申请一个双端队列
    queue.append(root)
    result = []

    # visited = set(root)                    # 因为是树的结构，所以只要向下走不会存在重复的情况

    while queue:
        level_size = len(queue)

        for _ in range(level_size):
            node = queue.popleft()  # 这里从左边出了，下面加入的时候就要加到末尾，若是从右边出，则下面从左边push进去
            result.append(node.val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    return result


def depth_first_search(root: TreeNode, result=[]) -> list:
    """
    二叉树广度优先遍历，返回广度遍历顺序
    :param root:
    :param result:
    :return:
    """

    if not root:
        return []

    result.append(root.val)
    depth_first_search(root.left, result)
    depth_first_search(root.right, result)
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

    print(pre_order(node4))

    print(in_order(node4))

    print(post_order(node4))

    print(breadth_first_search(node4))

    print(depth_first_search(node4))
