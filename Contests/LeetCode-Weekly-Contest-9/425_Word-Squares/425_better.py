class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        self.l = len(words[0])

        self.trie = self.build(words)

        self.res = []

        for word in words:
            self.dfs(words, self.trie, [word])

        return self.res

    def dfs(self, words, trie, lst):
        if len(lst) == self.l:
            self.res.append(lst)
            return

        prefix = ''
        for i in range(len(lst)):
            prefix += lst[i][len(lst)]

        for s in self.get(trie, prefix):
            self.dfs(words, trie, lst + [s])


    def build(self, words):
        trie = {}

        for word in words:
            t = trie

            for c in word:
                if c not in t:
                    t[c] = {}
                t = t[c]

            t['#'] = '#'

        return trie


    def get(self, trie, prefix):
        res = []

        t = trie
        for c in prefix:
            if c not in t:
                return res
            t = t[c]

        for s in self.getall(t):
            res.append(prefix + s)

        return res

    def getall(self, t):
        res = []
        if '#' in t: return ['']

        for c in t:
            if c != '#':
                for s in self.getall(t[c]):
                    res.append(c + s)
        return res
        
