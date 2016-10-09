class WordDictionary(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.root = Node("")

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        node = self.root
        for letter in word:
            child = node.addChild(letter)
            node = child
        node.setWordEnd()

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could
        contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        nodesToSearch = [self.root]
        for letter in word:
            if letter == ".":
                nextNodes = []
                for node in nodesToSearch:
                    nextNodes.extend(node.getChildren())
                nodesToSearch = nextNodes
            else:
                nextNodes = []
                for node in nodesToSearch:
                    child = node.getChild(letter)
                    if child:
                        nextNodes.append(child)
                if not nextNodes: # len == 0
                    return False
                nodesToSearch = nextNodes

        for node in nodesToSearch:
            if node.isWordEnd:
                return True
        return False

class Node():
    def __init__(self, letter):
        self.letter = letter
        self.children = dict()
        self.isWordEnd = False

    def addChild(self, letter):
        child = self.children.get(letter)
        if child:
            return child
        else:
            newChild = Node(letter)
            self.children[letter] = newChild
            return newChild

    def setWordEnd(self):
        self.isWordEnd = True

    # def getIsWordEnd(self):
    #     return self.isWordEnd

    def getChildren(self):
        children = []
        for key, child in self.children.iteritems():
            children.append(child)
        return children

    def getChild(self, letter):
        return self.children.get(letter)

    def printTrie(self):
        print self.letter, self.isWordEnd
        for key, child in self.children.iteritems():
            child.printTrie()





# Your WordDictionary object will be instantiated and called as such:
wordDictionary = WordDictionary()
wordDictionary.addWord("a")
print wordDictionary.search(".")
