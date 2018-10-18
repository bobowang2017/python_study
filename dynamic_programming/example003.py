# coding: utf-8
# n个物体的重量(w[0]无用)
w = [0, 2, 2, 6, 5, 4]
# n个物体的价值(p[0]无用)
p = [0, 6, 3, 5, 4, 6]
# 计算n的个数
n = len(w) - 1
# 背包的载重量
m = 10
# 装入背包的物体，元素为True时，对应物体被装入(x[0]无用)
x = [False for raw in range(n + 1)]
v = 0
# optp[i][j]表示在前i个物体中，能够装入载重量为j的背包中的物体的最大价值
optp = [[0 for col in range(m + 1)] for raw in range(n + 1)]
print(optp)