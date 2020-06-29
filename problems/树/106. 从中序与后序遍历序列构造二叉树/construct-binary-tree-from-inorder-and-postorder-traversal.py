# -*- coding:utf-8 -*-
#@Time  :    2020/6/27 7:21 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    construct-binary-tree-from-inorder-and-postorder-traversal.py
#@Description：https://leetcode-cn.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution():
    def buildTree_1(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not (inorder and postorder):
            return None

        root = TreeNode(postorder[-1])

        mid = inorder.index(postorder[-1])

        # 左子树
        root.left = self.buildTree(inorder[:mid], postorder[:mid])

        # 右子树
        root.right = self.buildTree(inorder[mid+1:], postorder[mid:-1])


        return root

    # 左右子树的顺序都可以
    def buildTree(self, inorder, postorder):
        print("buildTree()")
        def helper(inorder, postorder):
            print("helper():")
            # if there is no elements to construct subtrees
            if not (inorder and postorder):
                return None

            # 找到根的位置
            root = TreeNode(postorder[-1])

            mid = idx_map[root.val]-idx_map[inorder[0]]

            # build left subtree
            root.left = helper(inorder[:mid], postorder[:mid])

            # build right subtree
            root.right = helper(inorder[mid+1:], postorder[mid:-1])

            return root

        # build a hashmap value -> its index
        idx_map = {val: idx for idx, val in enumerate(inorder)}

        return helper(inorder, postorder)


    # 必须先右子树[官方解法]
    # def buildTree(self, inorder, postorder) -> TreeNode:
    #     print("buildTree()")
    #     def helper(in_left, in_right):
    #         print("helper():")
    #         # if there is no elements to construct subtrees
    #         if in_left > in_right:
    #             return None
    #
    #         # pick up the last element as a root
    #         val = postorder.pop()
    #         root = TreeNode(val)
    #
    #         # root splits inorder list
    #         # into left and right subtrees
    #         index = idx_map[val]
    #
    #         # build right subtree
    #         root.right = helper(index + 1, in_right)
    #         # build left subtree
    #         root.left = helper(in_left, index - 1)
    #         return root
    #
    #     # build a hashmap value -> its index
    #     idx_map = {val: idx for idx, val in enumerate(inorder)}
    #
    #     return helper(0, len(inorder) - 1)


if __name__ == '__main__':
    s = Solution()
    # 中序遍历
    inorder = [9, 3, 15, 20, 7]
    # inorder = [2, 3, 1]
    # 后序遍历
    # postorder = [3, 2, 1]
    postorder = [9, 15, 7, 20, 3]
    root = s.buildTree(inorder, postorder)
    print(root)