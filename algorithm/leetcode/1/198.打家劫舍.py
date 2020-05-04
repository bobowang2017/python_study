# -*- coding: utf-8 -*-
# 你是一个专业的小偷，计划偷窃沿街的房屋。每间房内都藏有一定的现金，影响你偷窃的唯一制约因素就是相邻的房屋装有相互连通的
# 防盗系统，如果两间相邻的房屋在同一晚上被小偷闯入，系统会自动报警。#
# 给定一个代表每个房屋存放金额的非负整数数组，计算你在不触动警报装置的情况下，能够偷窃到的最高金额。
#
# 示例 1:
# 输入: [1,2,3,1]
# 输出: 4
# 解释: 偷窃 1 号房屋 (金额 = 1) ，然后偷窃 3 号房屋 (金额 = 3)。
#      偷窃到的最高金额 = 1 + 3 = 4 。
# 示例 2:
# 输入: [2,7,9,3,1]
# 输出: 12
# 解释: 偷窃 1 号房屋 (金额 = 2), 偷窃 3 号房屋 (金额 = 9)，接着偷窃 5 号房屋 (金额 = 1)。
#      偷窃到的最高金额 = 2 + 9 + 1 = 12 。
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/house-robber
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def __init__(self):
        self.nums = None
        self.max = {}

    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        self.nums = nums
        result = self.display(0, 0)
        return result

    def display(self, idx, total):
        if idx > len(self.nums) - 1:
            return total
        if idx in self.max:
            return self.max[idx] + total
        num = self.nums[idx]
        get_current = self.display(idx + 2, total + num)
        no_current = self.display(idx + 1, total)
        self.max[idx] = max(get_current-total, no_current-total)
        print(idx, get_current, no_current)
        return max(get_current, no_current)


s = Solution()
res = s.rob([183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211])
print(res)
