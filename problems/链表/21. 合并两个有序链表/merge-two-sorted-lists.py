# -*- coding:utf-8 -*-
#@Time  :    2020/7/26 1:10 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    merge-two-sorted-lists.py
#@Description：https://leetcode-cn.com/problems/merge-two-sorted-lists/

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        def find_next_min_node(l1: ListNode, l2: ListNode):
            # 先设立递归终止条件
            if l1 == None:
                return l2
            if l2 == None:
                return l1
            # 比较两个指针的
            if l1.val > l2.val:
                minNode = l2
                l2 = l2.next
            else:
                minNode = l1
                l1 = l1.next

            minNode.next = find_next_min_node(l1, l2)

            return minNode

        node = find_next_min_node(l1, l2)

        return node

    # 官方解答
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

    # 官方解答

    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # 合并后 l1 和 l2 最多只有一个还未被合并完，我们直接将链表末尾指向未合并完的链表即可
        prev.next = l1 if l1 is not None else l2

        return prehead.next

if __name__ == '__main__':
    s = Solution()
    l1 = ListNode()
    l1.val = 4
    l2 = ListNode()
    l2.val = 4


    print(s.mergeTwoLists(l1,l2).next.val)






