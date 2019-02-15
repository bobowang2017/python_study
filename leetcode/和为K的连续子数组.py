# 给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。
#
# 示例 1 :
#
# 输入:nums = [1,1,1], k = 2
# 输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
# 说明 :
#
# 数组的长度为 [1, 20,000]。
# 数组中元素的范围是 [-1000, 1000] ，且整数 k 的范围是 [-1e7, 1e7]。


class Solution:
    def subarraySum(self, nums, k):
        sum = result = 0
        pre_sum = dict({0: 1})
        n = len(nums)
        for i in range(n):
            sum += nums[i]
            if sum - k in pre_sum:
                result += pre_sum.get(sum - k)
            pre_sum[sum] = pre_sum.get(sum, 0) + 1
        return result


solution = Solution()
result = solution.subarraySum([1, 2, 3, 4, 5, 1, 8, 4, 5, 6, 4], 10)
print(result)
