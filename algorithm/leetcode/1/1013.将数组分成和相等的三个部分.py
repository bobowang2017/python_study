# -*- coding: utf-8 -*-
# 给你一个整数数组 A，只有可以将其划分为三个和相等的非空部分时才返回 true，否则返回 false。
# 形式上，如果可以找出索引 i+1 < j 且满足 (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1]) 就可以将数组三等分。
# 示例 1：
# 输入：[0,2,1,-6,6,-7,9,1,2,0,1]
# 输出：true
# 解释：0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
# 示例 2：
# 输入：[0,2,1,-6,6,7,9,-1,2,0,1]
# 输出：false
# 示例 3：
# 输入：[3,3,6,5,-2,2,5,1,-9,4]
# 输出：true
# 解释：3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

# 解题思路
# 首选算A的累加和能否被3整除，不可以那分不了3等分。
# 双指针前后向中间逼近，不用考虑中间那段怎么分，只要左右两段累加和等于3等分的数值，中间剩的那段也就找到了。


class Solution(object):
    def canThreePartsEqualSum(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        _sum = sum(A)
        if _sum % 3 != 0:
            return False
        total = _sum // 3
        i, j = 0, len(A) - 1
        res = False
        l_total, r_total = A[0], A[len(A) - 1]
        while l_total != total and i < j:
            i += 1
            l_total += A[i]
        while r_total != total and i < j:
            j -= 1
            r_total += A[j]
        if i < j-1:
            res = True
        return res

s = Solution()
res = s.canThreePartsEqualSum([18,12,-18,18,-19,-1,10,10])
print(res)
