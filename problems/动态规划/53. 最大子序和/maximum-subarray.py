# -*- coding:utf-8 -*-
#@Time  :    2020/9/8 3:35 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    maximum-subarray.py
#@Description：

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = [0]*len(nums)
        dp[0] = nums[0]
        max_sum = dp[0]
        for i in range(1, len(nums)):
            dp[i] = max(nums[i], dp[i - 1] + nums[i])
            max_sum = max(max_sum, dp[i])
        return max_sum
