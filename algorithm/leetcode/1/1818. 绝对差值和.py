import math


class Solution(object):
    def minAbsoluteSumDiff(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: int
        """
        length = len(nums1)
        i = 0
        max_dis, index1 = 0, -1
        result_map = {}
        while i < length:
            res = abs(nums1[i] - nums2[i])
            if res > max_dis:
                max_dis = res
                index1 = i
            result_map[i] = res
            i += 1
        i, temp = 0, 1000000000
        index2 = -1
        while i < length:
            if i != index1:
                if abs(nums1[i] - nums2[index1]) < temp:
                    temp = abs(nums1[i] - nums2[index1])
                    index2 = i
            i += 1
        result_map[index1] = temp
        nums1[index1] = nums1[index2]
        print(nums1)
        print(nums2)
        print(sum(result_map.values()))
        return sum(result_map.values()) % (math.pow(10, 9) + 7)


# Solution().minAbsoluteSumDiff([1, 7, 5], [2, 3, 5])
# Solution().minAbsoluteSumDiff([2, 4, 6, 8, 10], [2, 4, 6, 8, 10])
# Solution().minAbsoluteSumDiff([1, 10, 4, 4, 2, 7], [9, 3, 5, 1, 7, 4])
Solution().minAbsoluteSumDiff([1, 28, 21], [9, 21, 20])
