# -*- coding:utf-8 -*-
#@Time  :    2020/8/25 2:15 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    test.py
#@Description：https://www.nowcoder.com/discuss/37372?type=0&order=0&pos=9&page=1


class Solution:
    def FindNumber(self,strr):
        if strr == "":
            return None
        dict_map = {}
        results = []
        for char in strr:
            if char in dict_map:
                time = dict_map[char]
                if time == 2:
                    results.append(char)
                dict_map[char] = time + 1
            else:
                dict_map[char] = 1

        for char in results:
             if dict_map[char] == 3:
                 return char

if __name__ == '__main__':
    s = Solution()
    strr = "cccaabcbbaa"
    print(s.FindNumber(strr))









