# coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

s = input()
for line in sys.stdin:
    each = line.strip().split(" ")
    n = int(each[0])
    m = int(each[1])
    if n==1 and m==1:
        print(1)
    if n>1 and m==1:
        print(0)

    dp = [0] * (n)
    dp[0] = m
    dp[1] = m*(m-1)
    for i in range(1,n):
        dp[i] = dp[i-1] * (m-1)
    print(dp[n-1]%(10^9+7))