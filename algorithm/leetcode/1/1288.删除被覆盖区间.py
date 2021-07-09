# -*- coding: utf-8 -*-
class Solution(object):
    def removeCoveredIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        intervals = sorted(intervals, key=lambda x: (x[0], -x[1]))

        count = 0
        max_right = 0
        for interval in intervals:
            if max_right < interval[1]:
                count += 1
                max_right = interval[1]
        return count


print(Solution().removeCoveredIntervals([[1, 4], [3, 6], [2, 8]]))
