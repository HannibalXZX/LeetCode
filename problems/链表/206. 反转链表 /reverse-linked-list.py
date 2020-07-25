# -*- coding:utf-8 -*-
#@Time  :    2020/7/24 10:25 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    reverse-linked-list.py
#@Description：https://leetcode-cn.com/problems/reverse-linked-list/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return None

        ## 记录倒转后的尾指针
        self.tail = None
        def get_next_node(preNode: ListNode):

            if preNode.next == None:
                self.tail = preNode
                return preNode

            # 获取下一个节点
            next_node = get_next_node(preNode.next)

            # 将下一个节点的指向改为指向上一个节点
            next_node.next = preNode

            # 上一个节点指向设置为空，禁止套娃
            preNode.next = None

            # 返回当前节点
            return preNode

        # 这一轮下来，反转了链表关系
        cur = get_next_node(head)

        return self.tail

    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # 申请两个节点，pre和 cur，pre指向None
        pre = None
        cur = head
        # 遍历链表，while循环里面的内容其实可以写成一行
        # 这里只做演示，就不搞那么骚气的写法了
        while cur:
            # 记录当前节点的下一个节点
            tmp = cur.next
            # 然后将当前节点指向pre
            cur.next = pre
            # pre和cur节点都前进一位
            pre = cur
            cur = tmp
        return pre


if __name__ == '__main__':
    l0 = ListNode(1)
    l1 = ListNode(2)
    l2 = ListNode(3)
    l0.next = l1
    l1.next = l2
    l2.next = None
    s = Solution()
    s.reverseList(l0)