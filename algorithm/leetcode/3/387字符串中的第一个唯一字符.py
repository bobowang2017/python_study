# 给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。
# 案例:
# s = "leetcode"
# 返回 0.
# s = "loveleetcode",
# 返回 2.
# 注意事项：您可以假定该字符串只包含小写字母。


class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        tmp = [0] * 26
        for ss in s:
            d = ord(ss) - ord('a')
            tmp[d] += 1
        for index, ss in enumerate(s):
            if tmp[ord(ss) - ord('a')] == 1:
                return index
        return -1


if __name__ == '__main__':
    s = Solution()
    result = s.firstUniqChar('leetcode')
    print(result)
