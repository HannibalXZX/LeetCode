# -*- coding:utf-8 -*-
#@Time  :    2020/7/29 5:24 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    remove-duplicate-letters.py
#@Description：https://leetcode-cn.com/problems/remove-duplicate-letters
from sympy.printing import str

class Solution:

    # 自我解法
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        count_char = Counter(s)

        stack = []
        for i in s:
            # 判断一下有没有加入到stack里面
            if i not in stack:
                while stack and i < stack[-1] and count_char[stack[-1]] > 0:
                    stack.pop()
                stack.append(i)
            # 剩余出现次数减1
            count_char[i] -= 1
            # 如果在栈里，我丢弃了。
            # 丢弃的原因是因为，先前的结果是最优的了（贪心的威力），我丢了就行。
        return "".join(stack)



if __name__ == '__main__':
    s =Solution()
    str = "bdb"
    print(s.removeDuplicateLetters(str))
