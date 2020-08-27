# -*- coding:utf-8 -*-
#@Time  :    2020/8/25 12:02 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    ce.py
#@Description：
from typing import List


class Solution:
    # 哈希表解法
    def majorityElement_1(self, nums: List[int]) -> int:
        dict_map = {}
        res = 0
        for i in nums:
            if i in dict_map:
                dict_map[i] += 1
            else:
                dict_map[i] = 1

        for key, value in dict_map.items():
            if value > len(nums)/2:
                return key
        return res

    # 票数和
    def majorityElement(self, nums: List[int]) -> int:
        votes = 0
        for num in nums:
            if votes == 0:
                x = num
                votes += 1
            else:
                if x == num:
                    votes += 1
                else:
                    votes -= 1

        return x

if __name__ == '__main__':
    s = Solution()
    # nums = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    nums = [3, 3, 4]
    # print(s.majorityElement_1(nums))
    print(s.majorityElement(nums))