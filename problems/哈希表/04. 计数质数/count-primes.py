# -*- coding:utf-8 -*-
#@Time  :    2020/7/21 11:43 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    count-primes.py
#@Description：https://leetcode-cn.com/problems/count-primes/

import math
class Solution:
    def is_prime(self, n):
        if n==1: return False
        if n == 2: return True
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return False
        return True

    def countPrimes_01(self, n: int) -> int:
        count = 0
        if n == 1:
            return 0
        for i in range(1, n):
            if self.is_prime(i):
                count +=1
        return count

    ## 厄拉多筛选算法
    def countPrimes(self, n: int) -> int:
        if n == 1 or n == 0 or n == 2: return 0
        count = 1
        b = [1] * n
        for i in range(3, n, 2):
            # 如果是质数
            if b[i]:
                j = 2
                while(i*j < n):
                    b[i*j] = 0
                    j += 1
                count += 1
            else:
                continue

        return count

if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(7))