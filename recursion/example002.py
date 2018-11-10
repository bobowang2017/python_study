# coding: utf-8
# 问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法？(改进版)
# 这个问题用递归很好解决。假设 f(n) 表示n级台阶的总跳数法，则有
# f(n) = f(n-1) + f(n - 2)。
# 不过对于可以使用递归解决的问题，我们一定要考虑是否有很多重复计算。显然对于 f(n) = f(n-1) + f(n-2) 的递归，是有很多重复计算的。
import time


def compute(n, tag):
    if 1 <= n <= 2:
        return n
    else:
        if tag[n] != 0:
            return tag[n]
        tag[n] = compute(n - 1, tag) + compute(n - 2, tag)
        return tag[n]


start = time.time()
tag = [0 for i in range(42)]
data = compute(40, tag)
end = time.time()
print(data)
print(end - start)
