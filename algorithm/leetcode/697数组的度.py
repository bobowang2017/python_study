# -*- coding: utf-8 -*-
class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = dict()
        for index, num in enumerate(nums):
            if num in res:
                res[num].append(index)
            else:
                res[num] = [index]
        d, du = 100000, -1
        for k, v in res.items():
            _len = len(v)
            if _len > du:
                du = _len
                if _len > 1:
                    d = v[-1] - v[0] + 1
            elif _len == du:
                if _len > 1:
                    _d = v[-1] - v[0] + 1
                    if _d < d:
                        d = _d
        return d if d != 100000 else 1


if __name__ == '__main__':
    s = Solution()
    res = s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])
    print(res)
