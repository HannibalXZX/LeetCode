# -*- coding:utf-8 -*-
#@Time  :    2020/3/9 0009 20:56
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    binary-tree-zigzag-level-order-traversal.py
#@Description：https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal/



class Solution(object):
    def zigzagLevelOrder(self, root):
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
        # 层级
        level = 1
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
                level += 1
                #  判断奇偶关系
                if level % 2 == 0:
                    list_tmp.reverse()
                    list_result.append(list_tmp)
                else:
                    list_result.append(list_tmp)

        return list_result