# -*- coding:utf-8 -*-
#@Time  :    2020/9/2 4:56 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    longest-common-subsequence.py
#@Description：https://leetcode-cn.com/problems/longest-common-subsequence/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n, m = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        return (dp[n][m])

if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "ace"
    s.longestCommonSubsequence(text1, text2)