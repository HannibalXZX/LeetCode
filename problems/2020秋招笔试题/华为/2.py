# -*- coding:utf-8 -*-
#@Time  :    2020/9/26 7:15 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    2.py.py
#@Description：


s = input()
# 依赖关系映射
rel_map = {}
# 所消耗时间映射
time_map = {}
# 解析一下字符串
list_group = s.strip().split(";")
bingfa = ""
# 构建依赖关系
# a_info = list_group[-1]
for g in list_group:
    # 解析为三部分
    fir, sec, third = g.split(":")
    # 对二、三部分，获取时间
    if "a" == fir:
        time, bingfa_str = third.split("/")
        time_map['a'] = int(time)
        num_bingfa = int(bingfa_str)
    else:
        # 对第二部分判断，去除首尾字符
        clean_sec = sec[1:-1]
        if "," in clean_sec:

        else:
            rel_map[fir] = clean_sec

