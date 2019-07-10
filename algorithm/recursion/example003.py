# coding: utf-8
# 问题：一只青蛙一次可以跳上1级台阶，也可以跳上2级。求该青蛙跳上一个n级的台阶总共有多少种跳法？(改进版)
# 这个问题用递归很好解决。假设 f(n) 表示n级台阶的总跳数法，则有
# f(n) = f(n-1) + f(n - 2)。
# 不过对于可以使用递归解决的问题，我们一定要考虑是否有很多重复计算。显然对于 f(n) = f(n-1) + f(n-2) 的递归，是有很多重复计算的。
# 对于example001、example002中的代码都是采用自顶向下，如果N比较大的时候，必须向下递归N层，所以可能导致栈空间不够用，可以采用自底向上的方法。
import time


def compute(n):
    if 1 <= n <= 2:
        return n
    f1 = 1
    f2 = 2
    sum = 0
    for i in range(3, n+1):
        sum = f1 + f2
        f1, f2 = f2, sum
    return sum


start = time.time()
data = compute(40)
end = time.time()
print(data)
print(end - start)
