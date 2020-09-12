# 数学题
# 过了55%的用例

def get_res(index, n):
    res = 0
    for i in range(1, n+1):
        res = res ^ (index % i)
    return res

# print(get_res(1, 2))

while 1:
    s1 = input()
    s2 = input()
    str_num = int(s1)
    a_list = s2.split(" ")
    b_list = []
    # 获取b的值
    for index, a in enumerate(a_list):
        res = get_res(index+1, str_num)
        b = int(a) ^ res
        b_list.append(b)
    res = 0
    for b in b_list:
        res = res ^ b

    print(res)






