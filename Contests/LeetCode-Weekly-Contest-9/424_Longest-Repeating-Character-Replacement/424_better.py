"""
Problem:    424. Longest Repeating Character Replacement
            https://leetcode.com/contest/9/problems/longest-repeating-character-replacement/
Language:   Python 2
Result:     Accepted
Author:     zhichenggu
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        table = {}
        res = 0
        p1 = p2 = 0
        while p2 < len(s):
            table[s[p2]] = table.get(s[p2], 0) + 1
            p2 += 1

            while sum(table.values()) - max(table.values()) > k:
                table[s[p1]] -= 1
                p1 += 1

            res = max(res, p2 - p1)

        return res
