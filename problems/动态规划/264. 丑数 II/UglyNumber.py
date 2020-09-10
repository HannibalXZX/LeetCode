# -*- coding:utf-8 -*-
#@Time  :    2020/9/10 7:15 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    UglyNumber.py
#@Description：https://leetcode-cn.com/problems/ugly-number-ii/

class Solution:

    def nthUglyNumber(self, n: int) -> int:
        if n == 1:
            return 1
        dp = [1] * n
        a, b, c = 0, 0, 0
        for i in range(1, n):
            n2, n3, n5 = dp[a]*2, dp[b]*3, dp[c]*5
            dp[i] = min(n2, n3, n5)
            if dp[i] == n2:
                a += 1
            if dp[i] == n3:
                b += 1
            if dp[i] == n5:
                c += 1
        return dp[-1]

    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        dp = [1]
        t2 = t3 = t5 = 0
        for i in range(index):
            ugly = min(min(dp[t2] * 2, dp[t3] * 3), dp[t5] * 5)
            if ugly == dp[t2] * 2:
                t2 += 1
            if ugly == dp[t3] * 3:
                t3 += 1
            if ugly == dp[t5] * 5:
                t5 += 1
            dp.append(ugly)
        return dp[index - 1]

if __name__ == '__main__':
    s = Solution()
    print(s.nthUglyNumber(10))