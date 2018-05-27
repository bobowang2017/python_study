# -*- coding: utf-8 -*-
# 给定一个正整数 n，找出小于或等于 n 的非负整数中，其二进制表示不包含 连续的1 的个数。
#
# 示例 1:
#
# 输入: 5
# 输出: 5
# 解释:
# 下面是带有相应二进制表示的非负整数<= 5：
# 0 : 0
# 1 : 1
# 2 : 10
# 3 : 11
# 4 : 100
# 5 : 101
# 其中，只有整数3违反规则（有两个连续的1），其他5个满足规则。
# 说明: 1 <= n <= 109


class Solution:
    def solve(self, n):
        if n == 0:
            return 1
        binary = bin(n)[2:]
        len = binary.__len__()
        f = list()
        f[0] = 1
        f[1] = 2
        for i in range(2, len + 1):
            f[i] = f[i - 1] + f[i - 2]
        sum = 0
        k = len
        for i in range(0, len):
            k -= 1
            if binary[i] == '1':
                sum += f[k - 1]
            if i > 0 and binary[i - 1] == '1':
                return sum
        sum += 1
        return sum


solution = Solution()
result = solution.solve(10000)
print(result)
