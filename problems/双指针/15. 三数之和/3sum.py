# -*- coding:utf-8 -*-
#@Time  :    2020/7/24 4:30 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    3sum.py
#@Description：

from typing import List

class Solution:

    # 暴力解法
    def threeSum_0(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        # 去重
        no_du_nums = list(set(nums))
        n = len(no_du_nums)
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if no_du_nums[i] + no_du_nums[j] +no_du_nums[k] == 0:
                        res.append([no_du_nums[i], no_du_nums[j], no_du_nums[k]])

        return res

    # 官方题解
    def threeSum_1(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()

        ans = list()

        for first in range(n):
            if first > 0 and nums[first] == nums[first-1]:
                continue

            third = n - 1
            target = -nums[first]

            for second in range(first + 1, n):
                if second > first + 1 and nums[second] == nums[second-1]:
                    continue

                while second < third and nums[second] + nums[third] > target:
                    third -= 1

                if second == third:
                    break

                if nums[second] + nums[third] == target:
                    ans.append([nums[first], nums[second], nums[third]])

        return ans

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()  # 先排序
        ans = []
        for first in range(n - 2):  # 枚举第一个元素
            if nums[first] > 0:
                break  # 数组里最小的都大于0 不可能有答案

            if first > 0 and nums[first] == nums[first - 1]:
                continue  # 保证first不会有重复

            # 以下作为标准双指针写法
            second, third = first + 1, n - 1
            while second < third:
                target = 0 - nums[first]
                s = nums[second] + nums[third]
                if s > target:  # 当前数值太大 做出决策：右指针左移
                    third -= 1  # 左移后有重复没关系 重复的就肯定又回来这里减1啦
                elif s < target:  # 当前数值太小 做出决策：左指针右移
                    second += 1
                else:  # 前数值正合适 做出决策：左指针右移且右指针左移 注意不能重复
                    ans.append([nums[first], nums[second], nums[third]])
                    second += 1
                    third -= 1

                    # 一直移动到和当前元素不相同的位置
                    while third > second and nums[third] == nums[third + 1]:
                        third -= 1

                    while third > second and nums[second] == nums[second - 1]:
                        second += 1
        return ans


if __name__ == '__main__':
    s = Solution()
    nums = [0,0,-1,-1,1]
    print(s.threeSum_0(nums))