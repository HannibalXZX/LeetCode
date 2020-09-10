# -*- coding:utf-8 -*-
#@Time  :    2020/9/9 9:40 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@Description：

# 排序数组中的不相邻数字之间的最大和

def test(nums):
    dp = [0] *len(nums)
    dp[0] = nums[0]
    dp[1] = max(nums[0], nums[1])
    for i in range(2, len(nums)):
        dp[i] = max(dp[i-2]+nums[i], dp[i-1])
    return dp[len(nums)-1]

test([1,2,3,4,5])