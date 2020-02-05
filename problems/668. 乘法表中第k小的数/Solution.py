# -*- coding:utf-8 -*-
#@Time  :    2020/2/4 22:38
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    search-insert-position.py
#@Description：



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
            count += min(num/i, n)

        print(count)
    # def findKthNumber(self, m, n, k):
    #     """
    #     :type m: int
    #     :type n: int
    #     :type k: int
    #     :rtype: int
    #     """
    #     # 处理边界问题
    #     if k == 1:
    #         return 1
    #     elif k == m*n:
    #         return m*n
    #     else:
    #         left = 1
    #         right = m*n
    #         while(left < right):
if __name__ == '__main__':
    s = Solution()
    s.count_smaller_than_num(3,3,6)