# -*- coding:utf-8 -*-
#@Time  :    2020/8/25 9:48 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    single-number.py
#@Description：https://leetcode-cn.com/problems/single-number/

from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        length = len(nums)
        if length == 0:
            return
        x = nums[0]
        for i in range(1, length):
            x = nums[i] ^ x
        return x

    def singleNumber(self, nums: List[int]) -> int:
        from functools import reduce
        return reduce(lambda x, y: x ^ y, nums)

if __name__ == '__main__':
    s = Solution()
    nums= [4,1,2,1,2]
    print(s.singleNumber(nums))
