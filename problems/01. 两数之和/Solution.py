# -*- coding:utf-8 -*-
#@Time  :    2020/2/2 20:41
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    Solution.py
#@Description：LeetCode-01


class Solution(object):
    # 2952 ms  12.6 MB O()
    def twoSum_01(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        lenth = len(nums)
        for i in range(lenth):
            for j in range(i+1, lenth):
                if nums[i] + nums[j] == target:
                    return [i, j]

if __name__ == '__main__':
    nums = [2, 7, 11, 15]
    target = 9
    s = Solution()
    print(s.twoSum_01(nums, target))