# -*- coding:utf-8 -*-
#@Time  :    2020/9/26 8:02 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    1.py
#@Description：


#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param matrix int整型二维数组
# @param m int整型
# @return int整型
#
class Solution:
    def kthSmallest(self, matrix, m):
        # 先排序
        li =[]
        for small_matrix in matrix:
            li.extend(small_matrix)

        return sorted(li)[m-1]

if __name__ == '__main__':
    s = Solution()
    matrix = [[1,5,8],[3,6,9],[7,10,13]]
    m = 8
    print(s.kthSmallest(matrix, m))