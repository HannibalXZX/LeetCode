# -*- coding:utf-8 -*-
#@Time  :    2020/7/23 11:09 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    climbing-stairs.py
#@Description：https://leetcode-cn.com/problems/climbing-stairs/



class Solution:
    # 动态规划
    def climbStairs_1(self, n: int) -> int:
        if n == 1: return 1
        if n == 0 : return 1
        dp = [0]*(n+1)
        # 假定给的值
        dp[0] = 1
        dp[1] = 1
        for i in range(2, n+1):
            dp[i] = dp[i-1] + dp[i-2]

        return dp[n]

    # 快速幂
    def climbStairs(self, n: int) -> int:
        import numpy as np
        a = np.array([[1, 1], [1, 0]])

        def helper(base, exp):
            if exp == 1:
                return base
            if exp == 0:
                # 返回单位矩阵
                return np.array([[1, 0], [0, 1]])

            result = helper(base, exp >> 1)
            result = np.dot(result, result)
            if exp & 1 == 1:
                result = np.dot(base, result)
            return result

        result = helper(a, n)
        # 列相加
        # f(n+1) = np.sum(result, axis=1)[0]
        f_n = np.sum(result, axis=1)[1]
        return int(f_n)


if __name__ == '__main__':
    s = Solution()
    n = 88
    print(s.climbStairs_1(n))
    print(s.climbStairs(n))