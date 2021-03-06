# -*- coding:utf-8 -*-
#@Time  :    2020/8/21 8:38 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    binary-tree-inorder-traversal.py
#@Description：https://leetcode-cn.com/problems/binary-tree-inorder-traversal/
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    # 递归
    def inorderTraversal_01(self, root: TreeNode) -> List[int]:
        nums = []
        def inorder(root:TreeNode):
            if root:
                inorder(root.left)
                nums.append(root.val)
                inorder(root.right)
            else:
                return
        inorder(root)
        return nums

    # 迭代
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [], []
        curr = root
        while stack or curr:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            output.append(curr.val)
            curr = curr.right

    ## 简洁方法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        stack, rst = [root], []
        while stack:
            i = stack.pop()
            if isinstance(i, TreeNode):
                stack.extend([i.right, i.val, i.left])
            elif isinstance(i, int):
                rst.append(i)
        return rst


    # 颜色标记法
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        WHITE, GRAY = 0, 1
        res = []
        stack = [(WHITE, root)]
        while stack:
            color, node = stack.pop()
            if node is None:
                continue
            if color == WHITE:
                stack.append((WHITE, node.right))
                stack.append((GRAY, node))
                stack.append((WHITE, node.left))
            else:
                res.append(node.val)
        return res


    # 通用模版【结合三种遍历方式，一起记忆】
    def inorderTraversal(self, root: TreeNode) -> List[int]:
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
                if p.right:
                    stack.append(p.right)  # 先append的最后访问
                stack.append(p)
                stack.append(None)
                if p.left:
                    stack.append(p.left)
        return result
