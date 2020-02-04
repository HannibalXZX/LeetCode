# -*- coding:utf-8 -*-
#@Time  :    2020/2/4 20:34
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    Solution.py
#@Description： https://leetcode-cn.com/problems/search-insert-position/

class Solution(object):
    # 遍历
    def searchInsert_01(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(len(nums)):
            if nums[i] < target and i < len(nums)-1:
                continue
            else:
                return i if nums[i] >= target else i+1

    # 分治法：直接考虑所有情况
    def searchInsert_02(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums)-1
        while(left <= right):
            mid = int((left + right)/2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return left

    # 分治法：提前判断
    def searchInsert_03(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        lenth = len(nums)
        if target > nums[lenth-1]:
            return lenth
        left = 0
        right = len(nums) - 1
        while (left < right):
            mid = int((left + right) / 2)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left

if __name__ == '__main__':
    nums = [1, 3]
    target = 2
    s = Solution()
    print(s.searchInsert_03(nums, target))