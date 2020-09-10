# -*- coding:utf-8 -*-
#@Time  :    2020/9/9 10:45 上午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    isomorphic-strings.py
#@Description：https://leetcode-cn.com/problems/isomorphic-strings/

class Solution:
    def Replace(self, ss: str, dic: dict) -> str:
        s1 = map(lambda x: dic[x], ss)
        # map这里返回的是迭代器，需要转换一下list
        list_s = [char for char in s1]
        return "".join(list_s)

    # 建立哈希映射表，但是这里需要两次
    def isIsomorphic(self, s: str, t: str) -> bool:
        dic_1 = {}
        dic_2 = {}
        for ss, tt in zip(s, t):
            dic_1[ss] = tt
            dic_2[tt] = ss
        strr_1 = self.Replace(s, dic_1)
        strr_2 = self.Replace(t, dic_2)
        # print(strr_1)
        # print(strr_2)
        if strr_1 == t and strr_2 == s:
            return True
        else:
            return False

if __name__ == '__main__':
    s1 = Solution()
    s = "egg"
    t = "add"
    # s = "ab"
    # t = "aa"
    s = "paper"
    t = "title"
    print(s1.isIsomorphic(t, s))