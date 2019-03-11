class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        import sys
        first = second = third = -sys.maxsize
        for num in nums:
            if num > first:
                first, second, third = num, first, second
            elif second < num < first:
                second, third = num, second
            elif third < num < second:
                third = num
        print(-sys.maxsize)
        return third if third != -sys.maxsize else first


if __name__ == '__main__':
    s = Solution()
    result = s.thirdMax([-2, 5, 3, -5, 2, -1])
    print(result)