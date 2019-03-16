class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        result = set()
        temp = dict()
        i, l = 0, len(nums)
        for i in range(l):
            a, b = nums[i] + k, nums[i] - k
            if nums[i] in temp:
                result.add((nums[i], nums[temp[nums[i]]]))
            else:
                temp[a] = i
                temp[b] = i
        print(temp)
        return len(result)


solution = Solution()
result = solution.findPairs([1, 2, 3, 4, 5], 1)
print(result)
