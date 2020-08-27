# -*- coding:utf-8 -*-
#@Time  :    2020/7/24 9:07 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    valid-parentheses.py
#@Description：https://leetcode-cn.com/problems/valid-parentheses/


class Solution:
    ## 初始版本
    def isValid_1(self, s: str) -> bool:
        hdx = { "}": "{", "]":"[",")": "("}
        stack = []
        for char in s:
            if char not in hdx:
                stack.append(char)
            else:
                if not stack:
                    return False
                top = stack.pop()
                if hdx[char] == top:
                    continue
                else:
                    return False

        if stack:
            return False
        else:
            return True

    ## 优化版本
    def isValid(self, s: str) -> bool:
        hdx = {"}": "{", "]": "[", ")": "(", "?": "?"}
        # 启用哨兵
        stack = ["?"]
        for char in s:
            if char not in hdx:
                stack.append(char)
            else:
                if not hdx[char] == stack.pop():
                    return False
        return len(stack) == 1

if __name__ == '__main__':
    solution = Solution()
    s = "?"
    print(solution.isValid(s))


