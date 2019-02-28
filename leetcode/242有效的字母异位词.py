# -*- coding: utf-8 -*-
class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        result1 = [0] * 26
        result2 = [0] * 26
        for s1 in s:
            result1[ord(s1) - ord('a')] += 1
        for s2 in t:
            result2[ord(s2) - ord('a')] += 1
        i = 0
        while i < 26:
            if result1[i] != result2[i]:
                return False
            i += 1
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.isAnagram("anagram", "nagaram")
    print(result)
