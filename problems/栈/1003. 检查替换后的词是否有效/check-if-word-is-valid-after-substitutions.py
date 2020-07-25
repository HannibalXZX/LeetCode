# -*- coding:utf-8 -*-
#@Time  :    2020/7/24 9:43 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    check-if-word-is-valid-after-substitutions.py
#@Description：https://leetcode-cn.com/problems/check-if-word-is-valid-after-substitutions/


class Solution:

    ## replace
    def isValid_1(self, S: str) -> bool:

        while(S):
            new_s = S.replace("abc", "")
            if len(new_s) == len(S):
                return False
            else:
                S = new_s

        return True

    ## stack
    def isValid(self, S: str) -> bool:
        stack = []
        for char in S:
            if char != "c":
                stack.append(char)
            else:
                if len(stack) < 2:
                    return False
                if stack[-1] == 'b' and stack[-2] == "a":
                    stack.pop()
                    stack.pop()
                else:
                    return False

        return len(stack) == 0


if __name__ == '__main__':
    sol= Solution()
    S = "b"
    print(sol.isValid(S))