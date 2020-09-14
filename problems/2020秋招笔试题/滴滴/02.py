# -*- coding:utf-8 -*-
#@Time  :    2020/9/13 7:59 下午
#@Author:    Shaw
#@mail  :    shaw@bupt.edu.cn
#@File  :    02.py
#@Description：

# 无向图的最小生成路径
# 使用Dijkstra算法求解

line1 = list(map(int,input().split()))
nodes = line1[0]
num_vertice = line1[1]

no_direct_graph = []
dis = {"src":0}

visited =[]
visited.append(src)

for i in nodes:
    dis[i] = graph[src][i]
path = {}