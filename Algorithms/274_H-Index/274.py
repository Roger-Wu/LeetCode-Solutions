class Solution(object):
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        citations.sort(reverse=True)
        h = 0
        for c in citations:
            if c >= h+1:
                h += 1
            else:
                break
        return h
