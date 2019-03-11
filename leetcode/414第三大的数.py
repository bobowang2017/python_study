class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        first = second = third = -65535
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif second < num < first:
                second, third = num, second
            elif third < num < second:
                third = num
        return third if third != -65535 else first


if __name__ == '__main__':
    s = Solution()
    result = s.thirdMax([-2, 5, 3, -5, 2, -1])
    print(result)