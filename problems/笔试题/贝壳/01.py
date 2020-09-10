# coding=utf-8
# 本题为考试单行多行输入输出规范示例，无需提交，不计分。
import sys

def compare(charA, charB):
    if charA == "S":
        if charB == "J":
            return 1
    if charA == "J":
        if charB == "B":
            return 1
    if charA == "B":
        if charB == "S":
            return 1
    return 0


print(compare("J","B"))
# sum = input()
#
for line in sys.stdin:
    each = line.strip().split(" ")
    left = compare(each[0], each[2]) + compare(each[0], each[3])
    right = compare(each[1], each[2]) + compare(each[1], each[3])
    if left == right:
        print("same")
    if left > right:
        print("left")
    if right > left:
        print("right")

