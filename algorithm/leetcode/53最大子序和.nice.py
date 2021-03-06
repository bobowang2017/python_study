# 给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。
# 示例:
# 输入: [-2,1,-3,4,-1,2,1,-5,4],
# 输出: 6
# 解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
# 进阶:如果你已经实现复杂度为 O(n) 的解法，尝试使用更为精妙的分治法求解。


class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_sub_sum = nums[0]
        for num in nums:
            sum += num
            if sum > max_sub_sum:
                max_sub_sum = sum
            if sum < 0:
                sum = 0
        return max_sub_sum


# 这个算法又称为Kadane算法，它是又美国卡耐基梅隆大学的教授Kadane发明的一种用于求解最大连续子序列和问题的最优算法。
# 对于一个长度为n的数组A而言，从A[0] 到 A[j] 是一个子数组（j<n），那么以A[j]结尾的子数组之最大和，要么是 A[j]，要
# 么是 max(A[i]~A[j-1])+A[j] ，其中0 ≤ i ≤ j-1。这就是该算法设计的出发点。

if __name__ == '__main__':
    s = Solution()
    result = s.maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4])
    print(result)
