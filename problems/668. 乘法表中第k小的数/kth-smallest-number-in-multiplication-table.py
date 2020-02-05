# -*- coding:utf-8 -*-
#@Time  :    2020/2/4 22:38
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    search-insert-position.py
#@Description： https://leetcode-cn.com/problems/kth-smallest-number-in-multiplication-table/


class Solution(object):

    # 在m*n乘法表中比num小的数字的数目
    def count_smaller_than_num(self,m, n, num):
        '''
        :type m: int
        :type n: int
        :type num: int
        :return: count int
        '''
        count = 0
        for i in range(1, m+1):
            count += min(int(num/i), n)
        return count

    # 在m*n乘法表中寻找第k小的数, 二分法, 错误解法
    def findKthNumber_wrong(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # 处理边界问题
        if k == 1:
            return 1
        elif k == m*n:
            return m*n
        else:
            left = 1
            right = m*n
            while(left < right):
                mid = int((left + right) >> 1)
                count_smaller_than_mid = self.count_smaller_than_num(m, n, mid)
                # 这里不能返回，因为此时的mid可能不在乘法表中
                if count_smaller_than_mid == k:
                    return mid
                elif count_smaller_than_mid < k:
                    left = mid + 1
                else:
                    right = mid

            return right

    # 在m*n乘法表中寻找第k小的数, 二分法
    def findKthNumber(self, m, n, k):
        """
        :type m: int
        :type n: int
        :type k: int
        :rtype: int
        """
        # 处理边界问题
        if k == 1:
            return 1
        elif k == m*n:
            return m*n
        else:
            left = 1
            right = m*n
            while(left < right):
                mid = int((left + right) >> 1)
                count_smaller_than_mid = self.count_smaller_than_num(m, n, mid)
                if count_smaller_than_mid < k:
                    left = mid + 1
                else:
                    right = mid

            return right

if __name__ == '__main__':
    s = Solution()
    m = 42
    n = 34
    k = 401
    # s.count_smaller_than_num(3,3,6)
    print(s.findKthNumber_wrong(m, n, k)) # 127
    print(s.findKthNumber(m, n, k)) # 126