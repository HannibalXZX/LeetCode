# -*- coding:utf-8 -*-
#@Time  :    2020/7/24 5:39 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    4sum.py
#@Description：https://leetcode-cn.com/problems/4sum/


from typing import List


class Solution:

    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        length = len(nums)
        res = []
        for first in range(length):

            if first > 0 and nums[first] == nums[first - 1]:
                continue  # 保证first不会有重复

            for second in range(first+1, length):

                if second > first+1 and nums[second] == nums[second-1]:
                    continue

                third = second + 1
                fourth = length - 1

                while(third < fourth):
                    sum = nums[first] + nums[second] + nums[third] + nums[fourth]
                    if sum < target:
                        third += 1
                    elif sum > target:
                        fourth -= 1
                    else:
                        res.append([nums[first], nums[second], nums[third], nums[fourth]])
                        third += 1
                        fourth -= 1
                        while fourth > third and nums[third] == nums[third-1]:
                            third += 1
                        while fourth > third and nums[fourth] == nums[fourth+1]:
                            fourth -= 1
        return res

if __name__ == '__main__':
    s = Solution()
    nums = [-1, 0, -5, -2, -2, -4, 0, 1, -2]
    target = -9
    print(s.fourSum(nums, target))









