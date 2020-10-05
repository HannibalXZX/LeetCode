# -*- coding:utf-8 -*-
#@Time  :    2020/9/3 3:07 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    sorted-merge-lcci.py
#@Description：https://leetcode-cn.com/problems/merge-sorted-array/

from typing import List

class Solution:

    def merge(self, A: List[int], m: int, B: List[int], n: int) -> None:
        """
        Do not return anything, modify A in-place instead.
        """
        tmp = []
        i = 0
        j = 0
        while i < m or j < n:
            if i == m:
                tmp.append(B[j])
                j += 1

            elif j == n:
                tmp.append(A[i])
                i += 1

            elif A[i] <= B[j]:
                tmp.append(A[i])
                i += 1
            else:
                tmp.append(B[j])
                j += 1

        # 细节 ，直接写成A=tmp是错误的
        # 简单来讲a[:]是深复制，a是浅复制，相当于赋值a的话是赋值了指针，赋值a[:]相当于复制了a对应的那段空间
        A[:] = tmp
        return A

    def merge_1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        tmp = []
        i, j = 0, 0
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp.append(nums1[i])
                i += 1

            else:
                tmp.append(nums2[j])
                j += 1
        if i < m:
            tmp.extend(nums1[i:m])
        if j < n:
            tmp.extend(nums2[j:n])
        nums1[:] = tmp
        # return tmp

if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    print(s.merge_1(A, m, B, n))