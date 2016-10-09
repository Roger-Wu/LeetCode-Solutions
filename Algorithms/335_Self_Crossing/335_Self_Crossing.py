class Solution(object):
    def isSelfCrossing(self, x):
        """
        :type x: List[int]
        :rtype: bool
        """
        l = len(x)

        if l < 4:
            return False

        """
        ┌───┐
        │   │
        └───┼──>
            │
        """
        for i in xrange(l-3):
            if x[i] - x[i+2] >= 0 and x[i+1] - x[i+3] <= 0:
                return True

        """
        ┌───┐
        │   │
        │   ^
        └───┘
        """
        if l >= 5:
            for i in xrange(l-4):
                if x[i] - x[i+2] + x[i+4] >= 0 and x[i+1] - x[i+3] == 0:
                    return True
        """
        ┌───┐
        │   │<─┐
        └──────┘
        """
        if l >= 6:
            for i in xrange(l-5):
                if (x[i] - x[i+2] < 0 and x[i+1] - x[i+3] < 0
                    and x[i] - x[i+2] + x[i+4] >= 0 and x[i] - x[i+2] + x[i+4] <= x[i]
                    and x[i+1] - x[i+3] + x[i+5] >= 0 and x[i+1] - x[i+3] + x[i+5] <= x[i+1]):
                    return True

        return False
