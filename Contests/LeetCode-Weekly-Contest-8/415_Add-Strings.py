"""
Problem:    415. Add Strings
            https://leetcode.com/contest/8/problems/add-strings/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        l = max([len(num1), len(num2)])
        num1 = num1.zfill(l)[::-1]
        num2 = num2.zfill(l)[::-1]

        result = []
        carry = 0
        for i in xrange(l):
            s = (ord(num1[i]) - ord('0')) + (ord(num2[i]) - ord('0')) + carry
            result.append(str(s % 10))
            carry = s / 10

        if carry > 0:
            result.append(str(carry))

        return str(''.join(result))[::-1]
