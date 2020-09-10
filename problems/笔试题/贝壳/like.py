#coding=utf-8
# 本题为考试多行输入输出规范示例，无需提交，不计分。
import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    str = sys.stdin.readline().strip()
    max_length = 0
    for i in range(n):
        tmp_str = str[0:i+1]
        if 2*i+2 >= n:
            break
        after_str = str[i+1:2*i+2]
        if tmp_str == after_str:
            common_length = i
            max_length = max(common_length, max_length)
    print(n-max_length)
