# -*- coding:utf-8 -*-
#@Time  :    2020/9/26 8:06 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    2.py
#@Description：

#
# 代码中的类名、方法名、参数名已经指定，请勿修改，直接返回方法规定的值即可
#
# @param nums int整型一维数组
# @return int整型
#
class Solution:
    def uniqueAward(self , nums ):
        # write code here
        length = len(nums)
        if length == 0:
            return
        x = nums[0]
        for i in range(1, length):
            x = nums[i] ^ x
        return x

if __name__ == '__main__':
    s  = Solution()
    nums = [3,2,2]
    print(s.uniqueAward(nums))