# -*- coding: utf-8 -*-
# 有面值分别为1，3，5的三种硬币若干，需要凑成11元最少需要多少硬币，凑成n元最少需要多少硬币？

temp_res = {}


def res_opt(n):
    if n in (1, 3, 5):
        return 1
    if n in temp_res:
        return temp_res[n]
    _a = res_opt(n - 1) + 1 if n > 1 else 0
    _b = res_opt(n - 3) + 1 if n > 3 else 0
    _c = res_opt(n - 5) + 1 if n > 5 else 0
    temp_res[n] = min(_a, _b, _c)
    return temp_res[n]


res = res_opt(100)
print(res)
