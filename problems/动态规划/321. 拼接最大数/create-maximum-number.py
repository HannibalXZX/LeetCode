# -*- coding:utf-8 -*-
#@Time  :    2020/7/31 3:55 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    create-maximum-number.py
#@Description：https://leetcode-cn.com/problems/create-maximum-number/
from typing import List


class Solution:

    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        m = len(nums1)
        n = len(nums2)
        if k > m+n:
            return

        max_list = []
        # 穷举有哪几种排列组合
        for i in range(0, min(m, k)+1):
                if k - i > n:
                    continue
                # 保存最大值
                c_list = self.merge(self.GetLargerNumByStack(nums1, i), self.GetLargerNumByStack(nums2, k-i))
                max_list = max(c_list, max_list)

        return max_list

    # 通过单调栈，筛选出了相对有序的k个最大数字
    def GetLargerNumByStack(self, nums:List[int], k:int) -> List[int]:
        if k == 0:
            return []
        stack = []
        drop = len(nums) - k

        for num in nums:
            while drop and stack and stack[-1] < num:
                stack.pop()
                drop -= 1
            stack.append(num)

        # 存在大于K的情况
        return stack[:k]

    # # # 插入排序
    # # 想复杂了，这是错误的解法！ 用自带的比较即可
    # def merge(self, nums1: List[int], nums2: List[int]) -> List:
    #     res = []
    #     while(nums1 and nums2):
    #         a = nums1[0]
    #         b = nums2[0]
    #
    #         if a > b:
    #             res.append(a)
    #             nums1 = nums1[1:]
    #         elif a < b:
    #             res.append(b)
    #             nums2 = nums2[1:]
    #         # a == b 需要继续比较下一个
    #         else :
    #             pass
    #     #          递归的形式
    #
    #     if not nums2:
    #         res.extend(nums1)
    #     else:
    #         res.extend(nums2)
    #     return res

    # 这里和合并两个有序链表还不一样，要保证最大值
    # 使用自带的比较即可
    def merge(self, A, B):
        ans = []
        while A or B:
            bigger = A if A > B else B
            ans.append(bigger[0])
            bigger.pop(0)
        return ans

    # 这里还要实现自带的比较,非完善
    # def cmp(self,A:List,B:List):
    #     i = 0
    #     while(A and B):
    #         if A[i] > B[i]:
    #             return A
    #         elif A[i] < B[i]
    #             return B
    #         else:
    #             i += 1
    #             continue

if __name__ == '__main__':
    s = Solution()

    nums1 = [3, 4, 6, 5]
    nums2 = [9, 1, 2, 5, 8, 3]
    k = 5

    nums1 = [6, 7]
    nums2 = [6, 0 ,4]
    k = 5
    # print(s.GetLargerNumByStack(nums1,3))

    # nums1 = [3, 9]
    # nums2 = [8, 9]
    # k = 3
    # [7,3,8,2,5,6,4,4,0,6,5,7,6,2,0]
    # nums1 =  [2, 5, 6, 4, 4, 0]
    # nums2 = [7, 3, 8, 0, 6, 5, 7, 6, 2]
    # k = 15

    # print(s.merge([6],[9, 5 ,8, 3]))
    # print(s.merge(nums1, nums2))
    #
    print(s.maxNumber(nums1, nums2, k))


