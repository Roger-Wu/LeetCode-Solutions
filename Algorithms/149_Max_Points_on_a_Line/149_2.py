# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# O(N^2) solution
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)

        if l <= 2:
            return l

        # idea:
        # find all the lines passing through a point,
        # find how many points are on each line, keep the max
        maxPointNum = 0
        for i in xrange(l-1):
            slopeToLineCount = dict()
            samePointsCount = 1 # this point must be on all lines passing through it
            maxPointOnLine = 0
            for j in xrange(i+1,l):
                if points[i].x == points[j].x and points[i].y == points[j].y:
                    samePointsCount += 1
                    continue

                slopeTuple = self.calcSlope(points[i],points[j])
                if slopeTuple in slopeToLineCount:
                    slopeToLineCount[slopeTuple] += 1
                else:
                    slopeToLineCount[slopeTuple] = 1

                maxPointOnLine = max(maxPointOnLine, slopeToLineCount[slopeTuple])

            maxPointNum = max(maxPointNum, samePointsCount + maxPointOnLine)

            # if current maxPointNum >= the num of remaining points, break
            if maxPointNum >= (l-i-1):
                break

        return maxPointNum

    def calcSlope(self, p1, p2):
        # return a tuple representing the slope
        dx = p2.x - p1.x
        dy = p2.y - p1.y
        if dx == 0 or dy == 0:
            return (int(dx != 0), int(dy != 0))
        gcd = self.gcd(dx,dy)
        return (dx/gcd, dy/gcd)

    def gcd(self, a, b):
        """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
        while b:
            a, b = b, a%b
        return a
