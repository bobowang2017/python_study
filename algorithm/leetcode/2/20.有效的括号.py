# 给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。
# 有效字符串需满足：
# 左括号必须用相同类型的右括号闭合。
# 左括号必须以正确的顺序闭合。
# 注意空字符串可被认为是有效字符串。


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if not s:
            return True
        if len(s) % 2 != 0:
            return False
        stack = list()
        for ss in s:
            if ss == '(' or ss == '[' or ss == '{':
                stack.append(ss)
            elif len(stack) == 0:
                return False
            elif (ss == ')' and stack[-1] == '(') or \
                    (ss == ']' and stack[-1] == '[') or \
                    (ss == '}' and stack[-1] == '{'):
                stack.pop(-1)
            else:
                return False
        if len(stack) != 0:
            return False
        return True


solution = Solution()
print(solution.isValid('(('))
