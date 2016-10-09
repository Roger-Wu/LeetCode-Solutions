class Trie(object):
    def __init__(self):
        self.root = [False]*27

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        node = self.root
        for char in word+'{':
            child = node[ord(char)-97]
            if not child:
                child = [False]*27
                node[ord(char)-97] = child
            node = child

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word+'{':
            child = node[ord(char)-97]
            if not child:
                print child
                return False
            node = child
        print node
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie
        that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            child = node[ord(char)-97]
            if not child:
                return False
            node = child
        return True
