# -*- coding: utf-8 -*-
# 给定一个数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。
# 滑动窗口每次只向右移动一位。
#
# 返回滑动窗口中的最大值。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/sliding-window-maximum
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        Q = deque()
        for idx, num in enumerate(nums):
            while len(Q) > 0 and nums[Q[-1]] <= num:
                Q.pop()
            Q.append(idx)
            if idx - Q[0] + 1 > k:
                Q.popleft()
            if idx >= k - 1:
                result.append(nums[Q[0]])
        return result


s = Solution()
print(s.maxSlidingWindow([6, 1, 3, -1, -3, 5, 3, 6, 7, 9, 4], 3))
