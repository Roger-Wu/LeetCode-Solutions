"""
https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
http://www.ruanyifeng.com/blog/2013/05/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm.html
"""


class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        # cheat
        # return haystack.find(needle)

        # KMP
        S = haystack
        W = needle

        if W == "":
            return 0
        elif S == "":
            return -1

        # Partial Match Table
        # see wikipedia
        T = [0] * len(W)
        T[0] = -1
        # prefixBegin = 0
        suffixBegin = 1
        matchLen = 0
        while suffixBegin + matchLen < len(W):
            T[suffixBegin + matchLen] = matchLen
            if W[suffixBegin + matchLen] == W[0 + matchLen]:  # prefixBegin + matchLen
                matchLen += 1
            else:
                # see https://youtu.be/KG44VoDtsAA?t=5m30s

                while True:
                    print suffixBegin, matchLen
                    suffixBegin += matchLen - T[matchLen]
                    matchLen = T[matchLen]
                    if W[suffixBegin + matchLen] == W[0 + matchLen]:
                        matchLen += 1
                        break
                    if matchLen == 0:
                        suffixBegin += 1
                        break

        # search
        m = 0
        i = 0
        while m+i < len(S):
            if S[m+i] == W[i]:
                i += 1
                if i == len(W):  # found
                    return m
            else:
                m += i - T[i]
                i = 0
        return -1
