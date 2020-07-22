# -*- coding:utf-8 -*-
#@Time  :    2020/7/22 7:16 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    number-of-1-bits.py
#@Description：https://leetcode-cn.com/problems/number-of-1-bits/

class Solution:
    def hammingWeight_1(self, n: int) -> int:
        count = 0
        while n:
            if n & 1 == 1:
                count += 1
            n = n >> 1

        return count

    def hammingWeight(self, n: int) -> int:
        count = 0
        while n:
            n = n & (n-1)
            count += 1

        return count
