# -*- coding:utf-8 -*-
#@Time  :    2020/9/5 7:16 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    22.py
#@Description：

# 礼物兑换
# 过了20%用例

class Solution:
    def getNumber(self, num):
        if num < 0:
            return 2 * num
        else:
            return num

    def numberofprize(self, a, b, c):
        res = 0

        while a > 0 and b > 0 and c > 0:
            a -= 1
            b -= 1
            c -= 1
            res += 1

        # print(res)
        sum = self.getNumber(a) + self.getNumber(b) + self.getNumber(c)

        while sum > 3:
            a = a - 1
            b = b - 1
            c = c - 1
            sum = self.getNumber(a) + self.getNumber(b) + self.getNumber(c)
            if sum >= 0:
                res += 1
                if a == -1:
                    a += 1
                if b == -1:
                    b += 1
                if c == -1:
                    c += 1
                if a > 0:
                    a -= 1
                if b >0 :
                    b -=1
                if c>0:
                    c-=1
                sum = self.getNumber(a) + self.getNumber(b) + self.getNumber(c)
            else:
                break

        return res

if __name__ == '__main__':
    s = Solution()
    a, b, c = 4, 4, 2
    a, b, c = 9, 3, 3
    a, b, c =  7,6,6
    print(s.numberofprize(a, b, c))