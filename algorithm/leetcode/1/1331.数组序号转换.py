# -*- coding: utf-8 -*-
class Solution(object):
    def arrayRankTransform(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        l = sorted(arr)
        temp = dict()
        total = 0
        for idx, _l in enumerate(l):
            if _l in temp:
                total +=1
            else:
                temp[_l] = idx - total
        return [temp[_a]+1 for _a in arr]


print(Solution().arrayRankTransform([37,12,28,9,100,56,80,5,12]))