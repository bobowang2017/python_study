# -*- coding: utf-8 -*-
# 给一非空的单词列表，返回前 k 个出现次数最多的单词。
# 返回的答案应该按单词出现频率由高到低排序。如果不同的单词有相同出现频率，按字母顺序排序。
# 示例 1：
# 输入: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
# 输出: ["i", "love"]
# 解析: "i" 和 "love" 为出现次数最多的两个单词，均为2次。
#     注意，按字母顺序 "i" 在 "love" 之前。
# 示例 2：
# 输入: ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4
# 输出: ["the", "is", "sunny", "day"]
# 解析: "the", "is", "sunny" 和 "day" 是出现次数最多的四个单词，
#     出现次数依次为 4, 3, 2 和 1 次。
# 注意：
# 假定 k 总为有效值， 1 ≤ k ≤ 集合元素数。
# 输入的单词均由小写字母组成。


class Solution(object):

    def sort(self, data):
        pass

    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        result = dict()
        for word in words:
            result[word] = 1 + result[word] if word in result.keys() else 1
        print(result)
        data = [(k, v) for (k, v) in sorted(result.items(), key=lambda n: (-n[1], n[0]))][:k]
        print(data)
        return list(map(lambda x: x[0], data))


solution = Solution()
result = solution.topKFrequent(["i", "love", "leetcode", "i", "love", "coding"], 3)
print(result)
