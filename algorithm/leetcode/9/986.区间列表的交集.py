# -*- coding: utf-8 -*-
class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        l1, l2 = len(firstList), len(secondList)
        i = j = 0
        while i < l1 and j < l2:
            x1, x2 = firstList[i][0], firstList[i][1]
            y1, y2 = secondList[j][0], secondList[j][1]
            if x1 <= y1 <= x2:
                if x2 < y2:
                    result.append([y1, x2])
                    i += 1
                else:
                    result.append([y1, y2])
                    j += 1
            elif y1 <= x1 <= y2:
                if x2 < y2:
                    result.append([x1, x2])
                    i += 1
                else:
                    result.append([x1, y2])
                    j += 1
            elif x1 < y1:
                i += 1
            else:
                j += 1
        return result


# print(Solution().intervalIntersection(
#     [[0, 2], [5, 10], [13, 23], [24, 25]],
#     [[1, 5], [8, 12], [15, 24], [25, 26]]
# ))
print(Solution().intervalIntersection(
    [[3, 5], [9, 20]],
    [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
))
