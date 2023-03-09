
class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        max_h = 0
        length = len(citations)
        idx = 0
        while idx < length:
            tmp = min(length - idx, citations[idx])
            if tmp > max_h:
                max_h = tmp
            idx += 1
        return max_h


print(Solution().hIndex([100]))
print(Solution().hIndex([0, 1, 3, 5, 6]))
print(Solution().hIndex([0, 0]))
print(Solution().hIndex([0, 1]))
print(Solution().hIndex([11, 15]))
