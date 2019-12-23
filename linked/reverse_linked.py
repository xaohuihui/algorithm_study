# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-6 
# @File     : reverse_linked.py
# Software  : algorithm_study

"""
反转链表
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# # 第一种解法
# def reverse_list(head: ListNode) -> ListNode:
#     if head and head.next:
#         a_list = list()
#         while head:
#             a_list.append(head)
#             head = head.next
#         start = a_list[-1]
#         for i in range(len(a_list) - 2, -1, -1):
#             a_list[i + 1].next = a_list[i]
#         a_list[0].next = None
#         return start
#     else:
#         return head

# # 第二种解法
# def reverse_list(head: ListNode) -> ListNode:
#     new_node = None
#     while head:
#         p = head.next          # 暂存下一个节点
#         head.next = new_node   # head指向上一个节点 上一个节点是从None开始
#         new_node = head        # new_node 向后移动到当前head位置
#         head = p               # head 向后移动一个节点
#     if not new_node:
#         return head
#     else:
#         return new_node

# # 第三种解法
def reverse_list(head: ListNode) -> ListNode:
    if head and head.next:
        p = reverse_list(head.next)
        head.next.next = head
        print("SSS", head.next.val, '\t', head.val)
        head.next = None
        return p

    else:
        return head


if __name__ == '__main__':
    # 1->2->3->4->5->NULL

    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = reverse_list(node1)

    while result:
        print("(", result.val, ")", end="\t")
        result = result.next
