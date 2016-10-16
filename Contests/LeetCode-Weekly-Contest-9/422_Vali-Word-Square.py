"""
Problem:    422. Valid Word Square
            https://leetcode.com/contest/9/problems/valid-word-square/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def validWordSquare(self, words):
        """
        :type words: List[str]
        :rtype: bool
        """
        for rowIdx in xrange(len(words)):
            for colIdx in xrange(len(words[rowIdx])):
                # check if words[colIdx][rowIdx] exist
                if colIdx >= len(words) or rowIdx >= len(words[colIdx]):
                    return False

                if words[rowIdx][colIdx] != words[colIdx][rowIdx]:
                    return False

        return True
