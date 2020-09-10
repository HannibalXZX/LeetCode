# -*- coding:utf-8 -*-
#@Time  :    2020/8/27 8:12 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    partition-list.py
#@Description：


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        ## 设置哑节点
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)

        while head:
            if head.val > x:
                after.next = head
                after = after.next
            else:
                before.next = head
                before = before.next

            head = head.next

        after.next = None
        before.next = after_head.next

        return before_head.next

