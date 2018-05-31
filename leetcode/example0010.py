# -*- coding: utf-8 -*-
# 给定一个非空字符串，其中包含字母顺序打乱的英文单词表示的数字0-9。按升序输出原始的数字。
# 注意:
# 输入只包含小写英文字母。
# 输入保证合法并可以转换为原始的数字，这意味着像 "abc" 或 "zerone" 的输入是不允许的。
# 输入字符串的长度小于 50,000。
# 示例 1:
# 输入: "owoztneoer"
# 输出: "012" (zeroonetwo)
# 示例 2:
# 输入: "fviefuro"
# 输出: "45" (fourfive)

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        example = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        data = list(s)

    def deal(self, s, result):
        temp_list = list(s)
        if 'o' in temp_list and 'n' in temp_list and 'e' in temp_list:
            s = s.replace('o', '', 1)
            s = s.replace('n', '', 1)
            s = s.replace('e', '', 1)
            result = result + ',' + 'one'
            self.deal(s, result)
        elif 't' in temp_list and 'w' in temp_list and 'o' in temp_list:
            s = s.replace('t', '', 1)
            s = s.replace('w', '', 1)
            s = s.replace('o', '', 1)
            result = result + ',' + 'two'
            self.deal(s, result)
        elif 't' in temp_list and 'h' in temp_list and 'r' in temp_list and 'e' in temp_list:
            s = s.replace('t', '', 1)
            s = s.replace('w', '', 1)
            s = s.replace('o', '', 1)
            result = result + ',' + 'two'
            self.deal(s, result)


solution = Solution()
result = solution.originalDigits("owoztneoer")
print(result)
