# -*- coding:utf-8 -*-
#@Time  :    2020/9/15 6:19 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    longest-increasing-subsequence.py
#@Description：https://leetcode-cn.com/problems/longest-increasing-subsequence/
from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        if not n:
            return 0
        dp = [1] * n
        for i in range(n):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j]+1)
        return max(dp)

if __name__ == '__main__':
    s = Solution()
    nums = [10,9,2,5,3,7,101,18]
    print(s.lengthOfLIS(nums))
