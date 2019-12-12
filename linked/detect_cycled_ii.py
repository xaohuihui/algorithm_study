# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-9 
# @File     : detect_cycled_ii.py
# Software  : study

"""
环形链表ii
"""


class ListNode:
    def __init__(self, x):
        self.x = x
        self.next = None


# Number.1
# def has_cycle(head: ListNode) -> ListNode:
#     result = None
#     if head and head.next:
#         set_node = set()
#         while head:
#             if head in set_node:
#                 result = head
#                 break
#             set_node.add(head)
#             head = head.next
#     return result

# NUmber.2
def has_cycle(head: ListNode) -> ListNode:
    result = None
    if head and head.next:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                fast = head
                break
        else:
            return result

        while fast != slow:
            fast = fast.next
            slow = slow.next
        result = fast
    return result


if __name__ == '__main__':
    # head=[3,2,0,4] pos= 1
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(4)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node1

    result_node = has_cycle(node1)
    if result_node:
        start = node1
        i = 0
        while start:
            if result_node == start:
                print(f"tail connects to node index {i}")
                break
            i += 1
            start = start.next
    else:
        print("no cycle")
