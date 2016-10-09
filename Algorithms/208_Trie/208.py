class TrieNode(object):
    def __init__(self, value="", isEnd=False):
        """
        Initialize your data structure here.
        """
        self.value = value
        self.children = {}
        self.isEnd = isEnd

    def setEnd(self):
        self.isEnd = True

    def addChild(self, char):
        return self.children.setdefault(char, TrieNode(char))

    def getChild(self, char):
        return self.children.get(char, None)


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word:
            node = node.addChild(char)
        node.setEnd()

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            node = node.getChild(char)
            if not node:
                return False
        return node.isEnd

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            node = node.getChild(char)
            if not node:
                return False
        return True


# Your Trie object will be instantiated and called as such:
# trie = Trie()
# trie.insert("somestring")
# trie.search("key")
