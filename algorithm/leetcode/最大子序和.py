# -*- coding: utf-8 -*-
# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
#
# 示例:
#
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。


class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        maxn = 0
        for num in nums:
            if sum >= 0:
                sum += num
            else:
                sum = num
            if sum > maxn:
                maxn = sum
        return maxn


if __name__ == '__main__':
    s = Solution()
    data = s.maxSubArray([-4, -1, -2, 1])
    print(data)
