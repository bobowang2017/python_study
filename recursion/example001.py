# coding: utf-8
# 问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法？
# 这个问题用递归很好解决。假设 f(n) 表示n级台阶的总跳数法，则有
# f(n) = f(n-1) + f(n - 2)。
import time


def compute(n):
    if 1 <= n <= 2:
        return n
    else:
        return compute(n - 1) + compute(n - 2)


start = time.time()
data = compute(35)
end = time.time()
print(data)
print(end - start)
