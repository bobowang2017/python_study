# -*- coding: utf-8 -*-
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip().split(' ')[-1])


if __name__ == '__main__':
    s = Solution()
    data = s.lengthOfLastWord("hello a ")
    print(data)
