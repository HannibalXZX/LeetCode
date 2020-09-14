# -*- coding:utf-8 -*-
#@Time  :    2020/9/13 7:43 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    01.py
#@Description：

# 解密字符串

while 1:
    n = int(input())
    sstr = input()
    length = len(sstr)
    res = []
    for i in range(0, length, n):
        # 这里不用判断越界
        tmp = sstr[i:i+n]
        print(tmp)
        res.extend(tmp[::-1])
    print("".join(res))
