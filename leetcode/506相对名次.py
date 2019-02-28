class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """

        temp = sorted(nums, reverse=True)
        temp_dict = {1: "Gold Medal", 2: "Silver Medal", 3: "Bronze Medal"}
        data = {data: temp_dict.get(index + 1, str(index + 1)) for index, data in enumerate(temp)}
        result = [data[num] for num in nums]
        return result