# -*- coding:utf-8 -*-
#@Time  :    2020/8/28 2:04 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    remove-duplicates-from-sorted-array.py
#@Description： https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array/

from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        length = len(nums)
        if length == 0:
            return
        # 双指针
        i = 0

        for j in range(i+1, length):
            if nums[i] == nums[j]:
                continue
            else:
                nums[i+1] = nums[j]
                i += 1

        return i+1

if __name__ == '__main__':
    s = Solution()
    nums = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(s.removeDuplicates(nums))




