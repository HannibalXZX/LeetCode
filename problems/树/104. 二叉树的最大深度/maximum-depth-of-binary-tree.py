# -*- coding:utf-8 -*-
# @Time  :    2020/2/7 10:32
# @Author:    Shaw
# @mail  :    shaw@bupt.edu.cn
# @File  :    longest-substring-without-repeating-characters.py
# @Description：https://leetcode-cn.com/problems/longest-substring-without-repeating-characters/

# Definition for a binary tree node.
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = TreeNode
        self.right = TreeNode

class Solution(object):

    # 递归
    def maxDepth_1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        left_height = self.maxDepth_1(root.left)
        right_height = self.maxDepth_1(root.right)
        return 1+max(left_height, right_height)

    def maxDepth_2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        stack = []
        stack.append((1, root))
        depth = 0
        while stack:
            current_depth, root = stack.pop()
            if root is not None:
                depth = max(current_depth, depth)
                stack.append((  + 1, root.left))
                stack.append((current_depth + 1, root.right))

        return depth

if __name__ == '__main__':
    tree = [3, 9, 20, None, None, 15,7]
