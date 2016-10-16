"""
Problem:    423. Reconstruct Original Digits from English
            https://leetcode.com/contest/9/problems/reconstruct-original-digits-from-english/
Language:   Python 2
Result:     Accepted
"""

from string import ascii_lowercase

class Solution(object):
    def originalDigits(self, s):
        """
        :type s: str
        :rtype: str
        """
        letterCount = dict()
        for letter in ascii_lowercase:
            letterCount[letter] = 0
        for c in s:
            letterCount[c] += 1

        numCount = [0] * 10

        # the order is important
        numCount[0] = letterCount['z']
        numCount[2] = letterCount['w']
        numCount[4] = letterCount['u']
        numCount[6] = letterCount['x']
        numCount[8] = letterCount['g']

        numCount[3] = letterCount['h'] - numCount[8]
        numCount[5] = letterCount['f'] - numCount[4]
        numCount[7] = letterCount['s'] - numCount[6]
        numCount[1] = letterCount['o'] - numCount[0] - numCount[2] - numCount[4]

        numCount[9] = letterCount['i'] - numCount[5] - numCount[6] - numCount[8]

        return ''.join([str(num)*numCount[num] for num in xrange(len(numCount))])
