# -*- coding:utf-8 -*-
#@Time  :    2020/8/22 12:15 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    binary-tree-postorder-traversal.py
#@Description：https://leetcode-cn.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        nums = []
        def postorder(root:TreeNode):
            if root.left:
                postorder(root.left)
            if root.right:
                postorder(root.right)
            if root:
               nums.append(root.val)
            else:
                return

        if root:
            postorder(root)
        return nums

    # 通用模版
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        result = []
        stack = [root]
        while stack:
            p = stack.pop()
            if p is None:
                p = stack.pop()
                result.append(p.val)
            else:
                stack.append(p)
                stack.append(None)
                if p.right:
                    stack.append(p.right)  # 先append的最后访问
                if p.left:
                    stack.append(p.left)
        return result
