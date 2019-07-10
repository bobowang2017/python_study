class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        template1 = {}.fromkeys('qwertyuiop', 1)
        template2 = {}.fromkeys('asdfghjkl', 2)
        template3 = {}.fromkeys('zxcvbnm', 3)
        template = {}
        template.update(template1)
        template.update(template2)
        template.update(template3)
        result = []
        for word in words:
            temp = True
            i, index = 1, template.get(word[0].lower())
            n = len(word)
            while i < n:
                if template.get(word[i].lower()) != index:
                    temp = False
                    break
                i += 1
            if temp:
                result.append(word)
        return result


if __name__ == '__main__':
    s = Solution()
    head = s.findWords(["Hello", "Alaska", "Dad", "Peace"])
    print(head)
