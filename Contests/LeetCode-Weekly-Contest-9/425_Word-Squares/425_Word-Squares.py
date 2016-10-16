"""
Problem:    425. Word Squares
            https://leetcode.com/contest/9/problems/longest-repeating-character-replacement/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def wordSquares(self, words):
        """
        :type words: List[str]
        :rtype: List[List[str]]
        """
        self.wordLen = len(words[0])
        if self.wordLen <= 1:
            return [[word] for word in words]

        self.eachCharDict = []
        for i in xrange(self.wordLen):
            charDict = dict()
            for char in string.lowercase:
                charDict[char] = []
            self.eachCharDict.append(charDict)
        for word in words:
            for i in xrange(self.wordLen):
                self.eachCharDict[i][word[i]].append(word)

        wordSquares = []
        for firstLineWord in words:
            psblWordsList = [self.eachCharDict[0][firstLineWord[i]] for i in xrange(1, self.wordLen)]
            subWordSquares = self.findWordSquares(psblWordsList)
            for subWordSquare in subWordSquares:
                ws = [firstLineWord]
                ws.extend(subWordSquare)
                wordSquares.append(ws)

        return wordSquares

    def findWordSquares(self, psblWordsList):
        size = len(psblWordsList)

        if size <= 1:
            return [[word] for word in psblWordsList[0]]

        if size >= 2:
            charStartIdx = self.wordLen - size
            addIdx = 0
            wordSquares = []
            for firstLineWord in psblWordsList[0]:
                newPsblWordsList = []
                for listIdx in xrange(1, size):
                    thisLinePsblWords = psblWordsList[listIdx]
                    newThisLinePsblWords = []
                    for psblWord in thisLinePsblWords:
                        if psblWord[charStartIdx] == firstLineWord[charStartIdx + listIdx]:
                            newThisLinePsblWords.append(psblWord)
                    newPsblWordsList.append(newThisLinePsblWords)
                subWordSquares = self.findWordSquares(newPsblWordsList)
                for subWordSquare in subWordSquares:
                    ws = [firstLineWord]
                    ws.extend(subWordSquare)
                    wordSquares.append(ws)

            return wordSquares
