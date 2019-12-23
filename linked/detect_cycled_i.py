# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-6 
# @File     : detect_cycled.py
# Software  : algorithm_study

"""
检测环形链表i
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# 第一种解法
# def has_cycle(head: ListNode) -> bool:
#     dict_node = dict()
#     i = 0
#     if head and head.next:
#         while head and head.next:
#             id_head = str(id(head))
#             if dict_node.get(id_head) is None:
#                 dict_node[id_head] = i
#             else:
#                 return True
#             i += 1
#             head = head.next
#         return False
#     else:
#         return False

# 第二种解法
def has_cycle(head: ListNode) -> bool:
    if head and head.next:
        fast = slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True

    else:
        return False


if __name__ == '__main__':
    # head=[3,2,0,4] pos= 1
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2

    print(has_cycle(node1))
