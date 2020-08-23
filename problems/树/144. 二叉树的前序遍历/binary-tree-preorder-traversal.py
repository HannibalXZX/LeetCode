# -*- coding:utf-8 -*-
#@Time  :    2020/8/21 7:29 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    binary-tree-preorder-traversal.py
#@Description：https://leetcode-cn.com/problems/binary-tree-preorder-traversal/


# Definition for a binary tree node.
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:

    ## 递归
    def preorderTraversal_0(self, root: TreeNode) -> List[int]:
        nums = []
        def preorder(root):
            if root:
                nums.append(root.val)
            else:
                return []
            if root.left:
                preorder(root.left)
            if root.right:
                preorder(root.right)
        preorder(root)
        return nums

    ## 迭代
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root], []
        while stack:
            root = stack.pop()
            if root is not None:
                output.append(root.val)
                if root.right is not None:
                    stack.append(root.right)
                if root.left is not None:
                    stack.append(root.left)
        return output

    # 通用模版【记忆】
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
                if p.right:
                    stack.append(p.right)  # 先append的最后访问
                if p.left:
                    stack.append(p.left)
                stack.append(p)
                stack.append(None)
        return result


if __name__ == '__main__':
    s = Solution()
    t = TreeNode(1)
    print(s.preorderTraversal(t))