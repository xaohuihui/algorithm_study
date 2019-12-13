# -*- coding: utf-8 -*-
# @Author   : xaohuihui
# @Time     : 19-12-12
# @File     : swap_pairs_linked.py
# Software  : study

"""
两两交换链表节点
"""


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# def swap_pairs(head: ListNode) -> ListNode:
#     pre = ListNode(0)
#     pre.next = head
#     tmp = pre
#     while tmp.next and tmp.next.next:
#         start = tmp.next  # “需要交换的第一个节点”
#         end = tmp.next.next  # “需要交换的第二个节点”
#
#         tmp.next = end    # “需要交换的第一个节点”的前面的一个节点，指向需要交换的第二个节点
#         start.next = end.next  # “需要交换的第一个节点”指向“需要交换的第二个节点”的后面的节点
#         end.next = start   # “需要交换的第二个节点”指向“需要交换的第一个节点”
#         # 上面交换完毕，现在start节点处于第二个节点的位置， end节点在第一个节点的位置
#         tmp = start  # 将tmp指向下一组“需要交换的第一个节点”的前面的一个节点， 即本次交换完成的第二个节点的位置
#
#     return pre.next

def swap_pairs(head: ListNode) -> ListNode:
    if head is None or head.next is None:   # 当长度为奇数时返回最后一个节点，当长度为偶数的时候返回None
        print(head.val if head else head)
        return head

    pre = head.next  # head 为“第一个需要交换节点”， pre 为“第二个需要交换的节点”
    print(head.val, pre.val)
    head.next = swap_pairs(pre.next)  # “第一个需要交换的节点” 指向 “第二个需要交换的节点”的后面的节点
    pre.next = head  # “第二个需要交换的节点” 指向 “第一个需要交换的节点”
    print("swap", head.val, pre.val, head.next.val if head.next else head.next)
    return pre


if __name__ == '__main__':
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(5)

    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5

    result = swap_pairs(node1)

    while result:
        print(result.val)
        result = result.next
