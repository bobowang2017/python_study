# 当前做法是通过前缀树匹配，比较麻烦
# 该题还可以通过字符串匹配依次比较每个元素，找出最小的即可
class TrieNode(object):
    def __init__(self):
        self.is_word = False
        self.idx = 10000
        self.children = {}


class Solution(object):
    def __init__(self):
        self.root = TrieNode()
        self.result = 10000

    def insert(self, idx, word):
        current_node = self.root
        for s in word:
            if s not in current_node.children:
                current_node.children[s] = TrieNode()
            current_node = current_node.children[s]
        current_node.is_word = True
        if idx < current_node.idx:
            current_node.idx = idx

    def display(self, node):
        if node.is_word:
            if node.idx < self.result:
                self.result = node.idx
                return
        for k, v in node.children.items():
            self.display(v)

    def search(self, search_str):
        current_node = self.root
        for _s in search_str:
            if _s in current_node.children:
                current_node = current_node.children[_s]
            else:
                self.result = -1
                return
        if current_node.is_word:
            self.result = current_node.idx
            return
        for k, child in current_node.children.items():
            self.display(child)
        return -1 if self.result == 10000 else self.result

    def isPrefixOfWord(self, sentence, searchWord):
        for idx, s in enumerate(sentence.split(" ")):
            self.insert(idx + 1, s)
        self.search(searchWord)
        return self.result


tree = Solution()
print(tree.isPrefixOfWord("love errichto jonathan dumb", "dumb"))
