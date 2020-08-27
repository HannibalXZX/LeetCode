# -*- coding:utf-8 -*-
#@Time  :    2020/2/2 23:21
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    search-insert-position.py
#@Description：https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

class Solution(object):
    # 已有工具numpy
    def findMedianSortedArrays_01(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        # 不用排序
        import numpy as np
        return np.median(nums1+nums2)

    #
    def findMedianSortedArrays_02(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """

if __name__ == '__main__':
    nums1 = [3]
    nums2 = [-1, -2]
    s = Solution()
    print(s.findMedianSortedArrays_01(nums1, nums2))



