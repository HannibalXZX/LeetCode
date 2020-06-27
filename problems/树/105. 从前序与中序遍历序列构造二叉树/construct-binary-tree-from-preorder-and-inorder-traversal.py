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

    # 构造哈希映射，帮助我们快速定位根节点
    def get_root_index(self, inorder):
        index = {element: index for index, element in enumerate(inorder)}



    # 使用自带的index函数
    def buildTree_01(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not (preorder and inorder):
            return None

        # 前序数组的第一个节点为根节点
        root = TreeNode(preorder[0])

        # 没有重复元素，可以直接用index函数找到中序遍历的根的位置
        mid = inorder.index(preorder[0])

        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


    # 构造哈希函数
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        if not (preorder and inorder):
            return None

        # 前序数组的第一个节点为根节点
        root = TreeNode(preorder[0])

        # TODO 可以优化，这里有时间复杂度
        # 没有重复元素，可以直接用index函数找到中序遍历的根的位置
        mid = inorder.index(preorder[0])

        # 构建左子树
        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])

        # 构建右子树
        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])

        return root


if __name__ == '__main__':
    s = Solution()
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    s.buildTree(preorder, inorder)




