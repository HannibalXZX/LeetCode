# -*- coding:utf-8 -*-
#@Time  :    2020/7/20 4:34 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    daily-temperatures.py
#@Description：https://leetcode-cn.com/problems/daily-temperatures/
from typing import List


class Solution:
    ## 官方题解
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        length = len(T)
        ans = [0] * length
        stack = []
        for i in range(length):
            temperature = T[i]
            while stack and temperature > T[stack[-1]]:
                prev_index = stack.pop()
                ans[prev_index] = i - prev_index
            stack.append(i)
        return ans

    ## 个人题解
    def dailyTemperatures_01(self, T):
        """
        :type T: List[int]
        :rtype: List[int]
        """
        ele_stack = []
        idx_stack = []
        ans = [0] * len(T)
        for index, element in enumerate(T):
            # empty stack
            if not ele_stack:
                ele_stack.append(element)
                idx_stack.append(index)
                continue

            # less than top element of the stack
            if element <= ele_stack[-1]:
                ele_stack.append(element)
                idx_stack.append(index)
                continue

            ## 写成循环
            while (ele_stack and element > ele_stack[-1]):
                pop_index = idx_stack.pop()
                ans[pop_index] = index - pop_index
                ele_stack.pop()

            # Don't Forget!
            ele_stack.append(element)
            idx_stack.append(index)

        return ans

if __name__ == '__main__':
    s = Solution()
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(s.dailyTemperatures_01(T))