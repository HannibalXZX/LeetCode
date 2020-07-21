# -*- coding:utf-8 -*-
#@Time  :    2020/7/21 8:07 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    wan-quan-ping-fang-shu-by-leetcode.py
#@Description：https://leetcode-cn.com/problems/perfect-squares/solution/wan-quan-ping-fang-shu-by-leetcode/


import math

class Solution:

    # 穷举法
    def numSquares_1(self, n: int) -> int:
        ## 获取所有完全平方数
        square_nums = [i**2 for i in range(1, int(math.sqrt(n)+1))]

        def minNumSquares(k):
            if k in square_nums:
                return 1
            min_num = float('inf')

            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                new_num = minNumSquares(k-square) + 1
                min_num = min(min_num, new_num)
            return min_num

        return minNumSquares(n)


    # 带存储的穷举法,仍然超时
    def numSquares_2(self, n: int) -> int:
        ## 获取所有完全平方数
        square_nums = [i**2 for i in range(1, int(math.sqrt(n)+1))]
        idx_map = {}
        def minNumSquares(k):
            if k in square_nums:
                idx_map[k] = 1
                return 1
            min_num = float('inf')
            # Find the minimal value among all possible solutions
            for square in square_nums:
                if k < square:
                    break
                if k-square in idx_map:
                    print(k-square)
                    new_num = idx_map[k-square] + 1
                else:
                    new_num = minNumSquares(k - square) + 1
                min_num = min(min_num, new_num)
                idx_map[k] = min_num
            return min_num

        return minNumSquares(n)

    # def isSquare(self, n: int) -> bool:
    #     sq = int(math.sqrt(n))
    #     return sq*sq == n

    # 动态规划
    def numSquares(self, n: int) -> int:
        square_nums = [i ** 2 for i in range(1, int(math.sqrt(n) + 1))]

        dp = [float('inf')] * (n+1)
        # bottom case
        dp[0] = 0
        for i in range(1, n+1):
            for square in square_nums:
                if i < square:
                    break
                dp[i] = min(dp[i], dp[i-square] + 1)

        return dp[-1]

    def numSquares(self, n: int) -> int:
        from collections import deque
        deq = deque()
        visited = set()

        deq.append((n, 0))
        while deq:
            number, step = deq.popleft()
            targets = [number - i * i for i in range(1, int(number ** 0.5) + 1)]
            for target in targets:
                if target == 0:
                    return step + 1
                if target not in visited:
                    deq.append((target, step + 1))
                    visited.add(target)
        return 0


if __name__ == '__main__':
    s = Solution()
    print(s.numSquares(7))

