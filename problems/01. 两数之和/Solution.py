# -*- coding:utf-8 -*-
#@Time  :    2020/2/2 20:41
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    Solution.py
#@Description：LeetCode-01


class Solution(object):
    # 穷举法
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

    # 列表哈希法
    def twoSum_02(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}
        for index, value in enumerate(nums):
            hashmap[value] = index
        for index, value in enumerate(nums):
            if (target - value) in hashmap:
                j = hashmap[target-value]
                if j != index:
                    return [index, j]

    # 列表哈希法
    def twoSum_03(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dct = {}
        for index, value in enumerate(nums):
            if target - value in dct:
                return [dct[target - value], index]
            dct[value] = index

if __name__ == '__main__':
    nums = [3, 2, 4, 15]
    target = 6
    s = Solution()
    print(s.twoSum_02(nums, target))