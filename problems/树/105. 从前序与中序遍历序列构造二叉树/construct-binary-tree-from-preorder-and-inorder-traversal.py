# -*- coding:utf-8 -*-
#@Time  :    2020/6/27 6:07 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    construct-binary-tree-from-preorder-and-inorder-traversal.py
#@Description： https://leetcode-cn.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):


    def __init__(self):
        self.count = 0

    # 使用自带的index函数
    def buildTree_1(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.count += 1
        # 这里非要标记括弧！
        if not (preorder and inorder):
            return None

        # 前序数组的第一个节点为根节点
        root = TreeNode(preorder[0])

        # 没有重复元素，可以直接用index函数找到中序遍历的根的位置
        mid = inorder.index(preorder[0])

        # 构建左子树
        root.left = self.buildTree_1(preorder[1:mid+1], inorder[:mid])

        # 构建右子树
        root.right = self.buildTree_1(preorder[mid+1:], inorder[mid+1:])

        return root


    # 构造哈希函数
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        self.count += 1

        def helper(preorder, inorder):
            self.count += 1

            if not (preorder and inorder):
                return None
            # 前序数组的第一个节点为根节点
            root = TreeNode(preorder[0])

            # 优化： 使用hash函数替代index函数
            mid = idx_map[root.val]-idx_map[inorder[0]]

            # 构建左子树
            root.left = helper(preorder[1:mid+1], inorder[:mid])

            # 构建右子树
            root.right = helper(preorder[mid+1:], inorder[mid+1:])

            return root

        # 要找中序的根节点位置

        idx_map = {val: index for index, val in enumerate(inorder)}
        return helper(preorder, inorder)


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    root = s.buildTree(preorder, inorder)
    print(s.count)





