# -*- coding: utf-8 -*-
# 给定一个整数数组和一个整数 k, 你需要在数组里找到不同的 k-diff 数对。这里将 k-diff 数对定义为一个整数对 (i, j),
# 其中 i 和 j 都是数组中的数字，且两数之差的绝对值是 k.
#
# 示例 1:
#
# 输入: [3, 1, 4, 1, 5], k = 2
# 输出: 2
# 解释: 数组中有两个 2-diff 数对, (1, 3) 和 (3, 5)。
# 尽管数组中有两个1，但我们只应返回不同的数对的数量。
# 示例 2:
#
# 输入:[1, 2, 3, 4, 5], k = 1
# 输出: 4
# 解释: 数组中有四个 1-diff 数对, (1, 2), (2, 3), (3, 4) 和 (4, 5)。
# 示例 3:
#
# 输入: [1, 3, 1, 5, 4], k = 0
# 输出: 1
# 解释: 数组中只有一个 0-diff 数对，(1, 1)。
# 注意:
#
# 数对 (i, j) 和数对 (j, i) 被算作同一数对。
# 数组的长度不超过10,000。
# 所有输入的整数的范围在 [-1e7, 1e7]。
#
# 来源：力扣（LeetCode）
# 链接：https://leetcode-cn.com/problems/k-diff-pairs-in-an-array
# 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。


class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k<0:
            return 0
        data = dict()
        total = 0
        res = set()
        for num in nums:
            a, b = num - k, k + num
            if a in data:
                total += 1
                res.add((max(a, num), min(a, num)))
            if b in data and a != b:
                total += 1
                res.add((max(b, num), min(b, num)))
            data[num] = 1
        return len(res)


s = Solution()
# res = s.findPairs([1, 2, 3, 4, 5], 3)
# res = s.findPairs([3, 1, 4, 1, 5], 2)
# res = s.findPairs([1, 2, 3, 4, 5], 1)
res = s.findPairs([1, 3, 1, 5, 4], 0)
print(res)
