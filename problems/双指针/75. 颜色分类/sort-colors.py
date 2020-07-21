# -*- coding:utf-8 -*-
#@Time  :    2020/7/21 4:19 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    sort-colors.py
#@Description：https://leetcode-cn.com/problems/sort-colors/


class Solution(object):
    def sortColors_1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作。
        # 直接修改了nums数组
        # 时间复杂度为O(n log n)
        # list.sort(nums) # 判断可

        # nums数组的本身值没有发生变化
        #
        nums1 = sorted(nums) # 编辑器无法通过，是个迷
        # print(nums1)
        return nums1

    def sortColors(self, nums):
        p1 = curr = 0
        p2 = len(nums) - 1
        while(curr<=p2):
            if nums[curr] == 2:
                nums[curr], nums[p2] = nums[p2], nums[curr]
                p2 -= 1
            elif nums[curr] == 0:
                nums[curr], nums[p1] = nums[p1], nums[curr]
                p1 += 1
                curr += 1
            else:
                curr += 1

        return nums
if __name__ == '__main__':
    s = Solution()
    nums = [1,2,0]
    print(s.sortColors(nums))