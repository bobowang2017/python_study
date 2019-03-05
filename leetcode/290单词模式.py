# 给定一种 pattern(模式) 和一个字符串 str ，判断 str 是否遵循相同的模式。
# 这里的遵循指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应模式。
# 示例1:
# 输入: pattern = "abba", str = "dog cat cat dog"
# 输出: true
# 示例 2:
# 输入:pattern = "abba", str = "dog cat cat fish"
# 输出: false
# 示例 3:
# 输入: pattern = "aaaa", str = "dog cat cat dog"
# 输出: false
# 示例 4:
# 输入: pattern = "abba", str = "dog dog dog dog"
# 输出: false
# 说明:
# 你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        if not pattern or not str:
            return False
        data = str.split(' ')
        if len(pattern) != len(data):
            return False
        tmp = dict()
        for index, p in enumerate(pattern):
            if p in tmp:
                if tmp[p] != data[index]:
                    return False
            else:
                if data[index] in tmp.values():
                    return False
                tmp[p] = data[index]
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.wordPattern("abba", "dog dog dog dog")
    print(result)
