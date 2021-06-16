class TrieNode(object):

    def __init__(self):
        self.end = 0
        self.path = 0
        self.map = [None for i in range(26)]


class TrieTree(object):
    def __init__(self):
        self.root = TrieNode()
        self.max_length = -1
        self.result = []

    def insert(self, word):
        if not word:
            return
        node = self.root
        for w in word:
            idx = ord(w) - ord('a')
            if not node.map[idx]:
                node.map[idx] = TrieNode()
            node = node.map[idx]
            node.path += 1
        node.end += 1

    def display(self, current_node, w):
        if len(w) > self.max_length:
            self.result.clear()
            self.result.append(w)
            self.max_length = len(w)
        elif len(w) == self.max_length:
            self.result.append(w)
        for idx, node in enumerate(current_node.map):
            if node and node.end != 0:
                self.display(node, w + chr(ord('a') + idx))


class Solution(object):
    def __init__(self):
        self.trie = TrieTree()

    def insert(self, word):
        self.trie.insert(word)

    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        if len(words) < 2:
            return ""
        for word in words:
            self.insert(word)
        self.display()
        if not self.trie.result:
            return ""
        return min(self.trie.result)

    def display(self):
        return self.trie.display(self.trie.root, "")


s = Solution()
res = s.longestWord(["w","wo","wor","worl", "world"])
print(res)
