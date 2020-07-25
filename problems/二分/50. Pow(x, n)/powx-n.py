# -*- coding:utf-8 -*-
#@Time  :    2020/7/23 12:04 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    powx-n.py
#@Description： https://leetcode-cn.com/problems/powx-n/

class Solution(object):
    def myPow_1(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        import math
        return math.pow(x, n)


    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """
        if abs(x)-0< 1e-7 and n == 0:
            return None
        pos_n = abs(n)

        def helper(x, n):
            if n == 1:
                return x
            if n == 0:
                return 1

            result = helper(x, n>>1)
            result = result * result
            if n & 1 == 1:
                result = x * result
            return result

        result = helper(x, pos_n)
        if n < 0:
            result = 1/result

        return result


if __name__ == '__main__':
    s = Solution()
    x, n = 2.00000, -2
    print(s.myPow(x, n))