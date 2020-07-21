# -*- coding:utf-8 -*-
#@Time  :    2020/7/20 10:12 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    next-greater-element-i.py
#@Description：


class Solution(object):
    # 个人解法，效率不高，可以AC
    def nextGreaterElement_1(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = [-1] * len(nums1)

        for i in range(len(nums1)):
            stack = []
            for element in nums2[::-1]:
                if element < nums1[i]:
                    continue
                elif element == nums1[i]:
                    if stack:
                        ans[i] = stack.pop()
                    else:
                        break
                else:
                    stack.append(element)
        return ans

    # 单调栈
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        ans = [-1] * len(nums1)
        stack = []
        dict_map = {}
        for element in nums2:
            while(stack and element>stack[-1]):
                top_element = stack.pop()
                dict_map[top_element] = element
            stack.append(element)

        for i in range(len(nums1)):
            if nums1[i] in dict_map:
                ans[i] = dict_map[nums1[i]]

        return ans

    # 速度更快
    def nextGreaterElement03(self, nums1, nums2):
        hash_dict = dict()
        stack = []
        for i in nums2:
            while stack and i > stack[-1]:
                hash_dict[stack.pop()] = i
            stack.append(i)
        return [hash_dict.get(i, -1) for i in nums1]


if __name__ == '__main__':
    s = Solution()
    nums1 = [4, 1, 2]
    nums2 = [1, 3, 4, 2]
    print(s.nextGreaterElement(nums1, nums2))