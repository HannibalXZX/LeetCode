# -*- coding:utf-8 -*-
#@Time  :    2020/7/29 3:19 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    remove-k-digits.py
#@Description：https://leetcode-cn.com/problems/remove-k-digits/


class Solution:

    def removeKdigits(self, num: str, k: int) -> str:
        if k == 0:
            return num
        if len(num) == k:
            return "0"

        stack = []
        for i in num:
            if k > 0:
                # 如果栈为空，则加入元素
                if not stack:
                    stack.append(i)
                    continue
                # 这里的出栈会导致stack为空
                while len(stack) and int(i) < int(stack[-1]) and k > 0:
                    stack.pop()
                    k -= 1
                stack.append(i)
            else:
                stack.append(i)

        if k > 0:
            stack = stack[:len(stack)-k]

        # 去除前导0
        while stack[0] == "0" and len(stack)>1:
            stack = stack[1:]
        return "".join(stack)

    def removeKdigits1(self, num: str, k: int) -> str:
        numStack = []

        # Construct a monotone increasing sequence of digits
        for digit in num:
            while k and numStack and numStack[-1] > digit:
                numStack.pop()
                k -= 1

            numStack.append(digit)

        # - Trunk the remaining K digits at the end
        # - in the case k==0: return the entire list
        finalStack = numStack[:-k] if k else numStack

        # trip the leading zeros
        return "".join(finalStack).lstrip('0') or "0"


if __name__ == '__main__':
    s = Solution()
    num = "1173"
    k = 2
    print(s.removeKdigits(num, k))