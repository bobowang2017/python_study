# -*- coding: utf-8 -*-
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums)
        if length == 0:
            return 0
        if length == 1:
            return nums[0]
        max_dp = [0 for _ in range(length)]
        min_dp = [0 for _ in range(length)]
        max_dp[0] = nums[0]
        min_dp[0] = nums[0]
        for i in range(1, length):
            max_dp[i] = max(max_dp[i - 1] * nums[i], nums[i], min_dp[i - 1] * nums[i])
            min_dp[i] = min(min_dp[i - 1] * nums[i], nums[i], max_dp[i - 1] * nums[i])
        return max(max_dp)


print(Solution().maxProduct([2, 3, -2, 4]))
print(Solution().maxProduct([-2,0,-1]))
