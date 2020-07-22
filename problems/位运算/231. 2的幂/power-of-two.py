# -*- coding:utf-8 -*-
#@Time  :    2020/7/22 7:18 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    power-of-two.py
#@Description：https://leetcode-cn.com/problems/power-of-twopower-of-two/


class Solution:
    ## 如果不限定负数，超出时间限制
    def isPowerOfTwo_1(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        while(n):
            if n & 1 == 1:
                count +=1

            n = n >> 1

        return True if count == 1 or count == 0 else False

    # 这里的循环多余了
    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False
        count = 0
        while(n):
            n = n & (n-1)
            count += 1
        return True if count == 1 or count == 0 else False

    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and n & (n - 1) == 0

    # 官方解答
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 0:
            return False
        return n & (-n) == n

if __name__ == '__main__':
    s = Solution()
    print(s.isPowerOfTwo(16))
