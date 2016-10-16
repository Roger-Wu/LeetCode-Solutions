"""
Problem:    424. Longest Repeating Character Replacement
            https://leetcode.com/contest/9/problems/longest-repeating-character-replacement/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        maxLen = 0
        ls = len(s)

        # find indices of characters
        charIdxs = dict()
        for i in xrange(len(s)):
            c = s[i]
            charIdxs[c] = charIdxs.get(c, [])
            charIdxs[c].append(i)

        for c, idxs in charIdxs.iteritems():
            # pointers of idxs
            begin = 0
            end = 0

            while end < len(idxs):
                strLen = (idxs[end] - idxs[begin] + 1)
                charCount = (end - begin + 1)
                needToReplace = strLen - charCount
                if needToReplace <= k:
                    outsideCanReplace = ls - strLen
                    outsideNeedReplace = k - needToReplace
                    strLenAfterReplace = strLen + min(outsideCanReplace, outsideNeedReplace)
                    maxLen = max(maxLen, strLenAfterReplace)

                    end += 1
                else:
                    begin += 1
                    if begin > end:
                        end = begin  # end += 1

        return maxLen
