class Solution(object):
    def __init__(self):
        self.map = {}

    def compare(self, word_a, word_b):
        length = min(len(word_a), len(word_b))
        for i in range(length):
            if self.map[word_a[i]] > self.map[word_b[i]]:
                return 1
            elif self.map[word_a[i]] == self.map[word_b[i]]:
                continue
            else:
                return -1
        if len(word_a) > len(word_b):
            return 1
        elif len(word_a) == len(word_b):
            return 0
        return -1

    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        for idx, o in enumerate(order):
            self.map[o] = idx

        for idx in range(len(words) - 1):
            if self.compare(words[idx], words[idx + 1]) <= 0:
                continue
            else:
                return False
        return True


s = Solution()
res = s.isAlienSorted(["apple","app"], "abcdefghijklmnopqrstuvwxyz")
print(res)
