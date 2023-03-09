# 和谐数组是指一个数组里元素的最大值和最小值之间的差别正好是1。
#
# 现在，给定一个整数数组，你需要在所有可能的子序列中找到最长的和谐子序列的长度。
#
# 示例 1:
#
# 输入: [1,3,2,2,5,2,3,7]
# 输出: 5
# 原因: 最长的和谐数组是：[3,2,2,2,3].
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/longest-harmonious-subsequence
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
import collections


class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = 0
        d = collections.Counter(nums)
        for num in nums:
            if num + 1 in d:
                ans = max(ans, d[num] + d[num + 1])
        return ans


s = Solution()
print(s.findLHS([1,3,2,2,5,2,3,7]))
