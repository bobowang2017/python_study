# -*- coding: utf-8 -*-

# 我们来定义一个函数 f(s)，其中传入参数 s 是一个非空字符串；该函数的功能是统计 s  中（按字典序比较）最小字母的出现频次。
#
# 例如，若 s = "dcce"，那么 f(s) = 2，因为最小的字母是 "c"，它出现了 2 次。
#
# 现在，给你两个字符串数组待查表 queries 和词汇表 words，请你返回一个整数数组 answer 作为答案，其中每个 answer[i] 是满足
# f(queries[i]) < f(W) 的词的数目，W 是词汇表 words 中的词。
import bisect


class Solution:
    def numSmallerByFrequency(self, queries, words):
        f = lambda x: x.count(min(x))
        n, ws = len(words), sorted(map(f, words))
        return [n - bisect.bisect(ws, i) for i in map(f, queries)]


s = Solution()
print(s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]))
