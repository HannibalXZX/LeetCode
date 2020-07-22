# -*- coding:utf-8 -*-
#@Time  :    2020/7/22 5:57 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    integer-break.py
#@Description：https://leetcode-cn.com/problems/integer-breakinteger-break/
class Solution(object):

    ## 书上的动态规划
    def cuttingRope_1(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2
        products = [0] * (n+1)
        products[0] = 0
        products[1] = 1
        products[2] = 2
        products[3] = 3

        for i in range(4, n+1):
            max = 0
            for j in range(1, int(i/2)+1):
                product = products[j] * products[i-j]
                if max < product:
                    max = product

                products[i] = max

        max = products[n]

        return max

    # 贪婪算法
    def cuttingRope(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0
        if n == 2:
            return 1
        if n == 3:
            return 2

        timeOf3 = n // 3

        if n % 3 == 0:
            max = pow(3, timeOf3)
        elif n % 3 == 1:
            max = pow(3, timeOf3-1) * 4
        else:
            max = pow(3, timeOf3) * 2

        return max


if __name__ == '__main__':
    s = Solution()
    print(s.cuttingRope(10))