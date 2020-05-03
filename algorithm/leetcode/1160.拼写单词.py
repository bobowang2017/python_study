# -*- coding: utf-8 -*-
# 给你一份『词汇表』（字符串数组） words 和一张『字母表』（字符串） chars。
#
# 假如你可以用 chars 中的『字母』（字符）拼写出 words 中的某个『单词』（字符串），那么我们就认为你掌握了这个单词。
#
# 注意：每次拼写（指拼写词汇表中的一个单词）时，chars 中的每个字母都只能用一次。
#
# 返回词汇表 words 中你掌握的所有单词的 长度之和。
#
#  
#
# 示例 1：
#
# 输入：words = ["cat","bt","hat","tree"], chars = "atach"
# 输出：6
# 解释：
# 可以形成字符串 "cat" 和 "hat"，所以答案是 3 + 3 = 6。
# 示例 2：
#
# 输入：words = ["hello","world","leetcode"], chars = "welldonehoneyr"
# 输出：10
# 解释：
# 可以形成字符串 "hello" 和 "world"，所以答案是 5 + 5 = 10。
#  
#
# 提示：
#
# 1 <= words.length <= 1000
# 1 <= words[i].length, chars.length <= 100
# 所有字符串中都仅包含小写英文字母
import copy


class Solution(object):
    def countCharacters(self, words, chars):
        """
        :type words: List[str]
        :type chars: str
        :rtype: int
        """
        template = dict()
        for c in chars:
            if c in template:
                template[c] += 1
            else:
                template[c] = 1
        result = 0
        for word in words:
            copy_template = copy.deepcopy(template)
            tag = True
            for w in word:
                if w in copy_template and copy_template[w] > 0:
                    copy_template[w] -= 1
                else:
                    tag = False
                    break
            if tag:
                result += len(word)
        return result


s = Solution()
# result = s.countCharacters(["cat", "bt", "hat", "tree"], "atach")
result = s.countCharacters(["hello","world","leetcode"], "welldonehoneyr")
print(result)
