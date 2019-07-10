class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        l = len(nums) + 1
        tmp = [0] * l
        for num in nums:
            if 1 <= num and num <= l:
                tmp[num] += 1
        result = []
        for index, t in enumerate(tmp):
            if t == 0 and index != 0:
                result.append(index)
        return result