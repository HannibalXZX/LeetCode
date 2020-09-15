# -*- coding:utf-8 -*-
#@Time  :    2020/9/3 3:07 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    sorted-merge-lcci.py
#@Description：
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

        A[:] = tmp
        return A

if __name__ == '__main__':
    s = Solution()
    A = [1, 2, 3, 0, 0, 0]
    m = 3
    B = [2, 5, 6]
    n = 3
    print(s.merge(A, m, B, n))