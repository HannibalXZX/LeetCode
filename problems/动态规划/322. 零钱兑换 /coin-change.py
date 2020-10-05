# -*- coding:utf-8 -*-
#@Time  :    2020/7/31 7:26 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    coin-change.py
#@Description：https://leetcode-cn.com/problems/coin-change/

from typing import List
class Solution:
    def coinChange_1(self, coins: List[int], amount: int) -> int:
        # 1、初始化数组
        dp = [float('inf')] * (amount + 1)
        # 定义dp[i]含义，表示数额为i时的最少硬币个数
        dp[0] = 0
        # 迭代，优化的穷举
        # 循环的摆放是细节,循环兑换时，会出现御姐
        for i in range(0, amount+1):
            for coin in coins:
                # 这里有个bug, i - coin 会越界
                # IndexError: list index out of range
                # if i - coin < 0 :
                print(dp[i-coin])
                dp[i] = min(dp[i], dp[i-coin]+1)

        return dp[amount] if dp[amount] != float('inf') else -1

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0

        # 循环的摆放是细节
        for coin in coins:
            for x in range(coin, amount + 1): # 细节
                dp[x] = min(dp[x], dp[x - coin] + 1)
        return dp[amount] if dp[amount] != float('inf') else -1


if __name__ == '__main__':
    s = Solution()
    coins = [1, 2, 5]
    amount = 11
    # coins = [213123124]
    # amount = 2
    print(s.coinChange(coins, amount))
    # print(s.coinChange_1(coins, amount))