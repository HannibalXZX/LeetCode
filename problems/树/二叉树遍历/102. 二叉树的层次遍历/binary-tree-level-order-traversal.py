# -*- coding:utf-8 -*-
# @Time  :    2020-3-8 19:53:30
# @Author:    Shaw
# @mail  :    shaw@bupt.edu.cn
# @File  :    binary-tree-level-order-traversal.py
# @Description：https://leetcode-cn.com/problems/binary-tree-level-order-traversal/

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):

    ## 递归
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        res = []
        def helper(root, depth):
            if not root: return
            if len(res) == depth:
                res.append([])
            res[depth].append(root.val)
            helper(root.left, depth + 1)
            helper(root.right, depth + 1)

        helper(root, 0)
        return res


    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if root == None:
          return []
        # 队列实现
        from collections import deque
        list_result = [[root.val]]
        # deque中必须添加一个迭代器
        Qresult = deque()
        Qresult.append([root, ])
        # 出队列
        while len(Qresult):
             # 当前队列还有的元素个数
             current_count = len(Qresult)
             list_tmp = []
             for i in range(current_count):
                #  这边要出队首元素
                _TreeNode = Qresult.popleft()[0]
                if _TreeNode.left:
                    list_tmp.append(_TreeNode.left.val)
                    Qresult.append([_TreeNode.left, ])
                if _TreeNode.right:
                    list_tmp.append(_TreeNode.right.val)
                    Qresult.append([_TreeNode.right, ])
             if list_tmp:
                list_result.append(list_tmp)

        return list_result

    ## 模版

