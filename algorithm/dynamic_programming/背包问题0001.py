# coding: utf-8
# 前i个物品装入容量为j的背包中获得的最大价值

__author__ = 'bobo'


def bag(n, c, w, v) -> "n 是个数，c是背包最大容量，w是物品的的重量，v是物品的价值":
    w.insert(0, 0)
    v.insert(0, 0)  # 为了是序号跟res保持同步，因为res是从1开始计算的
    res = [[-1 for i in range(c + 1)] for j in range(n + 1)]
    display(res)
    for j in range(c + 1):
        res[0][j] = 0
    display(res)
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            if j < w[i]:
                res[i][j] = res[i - 1][j]
            else:
                res[i][j] = max((res[i - 1][j], res[i - 1][j - w[i]] + v[i]))
        display(res)
    return res


def display(res):
    print('*' * 50)
    for data in res:
        print(data)
    print('*' * 50)


def show(n, c, w, res):
    print('最大价值为:', res[n][c])
    x = [False for i in range(n)]
    j = c
    for i in range(n, 0, -1):
        if res[i][j] > res[i - 1][j]:
            x[i - 1] = True
            j -= w[i - 1]
    print('选择的物品为:')
    for i in range(n):
        if x[i]:
            print('第', i, '个,')
    print('')


if __name__ == '__main__':
    # 物品数量
    n = 5
    # 背包最大容量
    c = 10
    # 物品重量
    w = [2, 2, 6, 5, 4]
    # 物品价值
    v = [6, 3, 5, 4, 6]
    res = bag(n, c, w, v)
    show(n, c, w, res)
