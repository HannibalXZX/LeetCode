# -*- coding:utf-8 -*-
#@Time  :    2020/8/28 5:18 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    valid-palindrome.py
#@Description：https://leetcode-cn.com/problems/valid-palindrome/


class Solution:
    def isPalindrome(self, s: str) -> bool:
        ss = [char for char in s if char.isalpha() or char.isalnum()]
        length = len(ss)
        i = 0
        j = length - 1
        while i <= j:
            if ss[i].lower() == ss[j].lower():
                i += 1
                j -= 1
            else:
                return False
        return True

    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        return sgood == sgood[::-1]

    def isPalindrome(self, s: str) -> bool:
        sgood = "".join(ch.lower() for ch in s if ch.isalnum())
        n = len(sgood)
        left, right = 0, n - 1

        while left < right:
            if sgood[left] != sgood[right]:
                return False
            left, right = left + 1, right - 1
        return True

    def isPalindrome(self, s: str) -> bool:
        n = len(s)
        left, right = 0, n - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if left < right:
                if s[left].lower() != s[right].lower():
                    return False
                left, right = left + 1, right - 1
        return True


if __name__ == '__main__':
    so = Solution()
    s = "A man, a plan, a canal: Panama"
    # s = "1234"
    s = ".,"
    print(so.isPalindrome(s))
