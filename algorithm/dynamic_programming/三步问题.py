# -*- coding: utf-8 -*-
# 三步问题。有个小孩正在上楼梯，楼梯有n阶台阶，小孩一次可以上1阶、2阶或3阶。实现一种方法，计算小孩有多少种上楼梯的方式。
# 结果可能很大，你需要对结果模1000000007。
# 示例1:
#  输入：n = 3
#  输出：4
#  说明: 有四种走法
# 示例2:
#  输入：n = 5
#  输出：13
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/three-steps-problem-lcci
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def __init__(self):
        self.arr = None

    def dp(self, n):
        if n == 0 or n == 1:
            return 1
        if n == 2:
            return 2
        if self.arr[n] != -1:
            return self.arr[n]
        res = (self.dp(n - 1) + self.dp(n - 2) + self.dp(n - 3)) % 1000000007
        return res

    def waysToStep(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.arr = [-1 for i in range(n + 1)]
        self.arr[0] = 1
        self.arr[1] = 1
        self.arr[2] = 2
        for i in range(3, n+1):
            print(i)
            self.arr[i] = (self.arr[i - 1] + self.arr[i - 2] + self.arr[i - 3]) % 1000000007
        return self.arr[n]


s = Solution()
print(s.waysToStep(5))
