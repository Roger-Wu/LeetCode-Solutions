# Definition for a point.
# class Point(object):
#     def __init__(self, a=0, b=0):
#         self.x = a
#         self.y = b

# O(N^3) solution
class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[Point]
        :rtype: int
        """
        l = len(points)

        if l <= 2:
            return l

        # line = (point1, point2)
        # if point3 is on line, then (point3 - point1) = k (point3 - point2)
        lines = []  # each line should be unique
        lineIdxToPointIdxs = [] # as dict: { 0:[0,1,3,6], 1:[0,2], 2:[0,4,5], ... }
        pointIdxToLineIdxs = [] # as dict: { 0:[0,1,2], 1:[0,...], 2:[1,...], ... }

        # init pointIdxToLineIdxs
        for i in xrange(l):
            pointIdxToLineIdxs.append([])

        for i in xrange(l):
            for j in xrange(i+1,l):
                # check if both points have been on another line
                isBothOnAnotherLine = False
                linesThroughP1 = pointIdxToLineIdxs[i]
                linesThroughP2 = pointIdxToLineIdxs[j]
                for lIdx in linesThroughP1:
                    if lIdx in linesThroughP2:
                        isBothOnAnotherLine = True
                        break
                if isBothOnAnotherLine:
                    continue

                # if points are not on a existing line, create a line through them
                line = (points[i], points[j])
                lines.append( line )
                lineIdx = len(lines) - 1

                # update the two dict
                lineIdxToPointIdxs.append([i,j])
                pointIdxToLineIdxs[i].append(lineIdx)
                pointIdxToLineIdxs[j].append(lineIdx)

                # check if other points are also on this line
                for k in xrange(j+1,l):
                    if self.pointOnLine(points[k], line):
                        lineIdxToPointIdxs[lineIdx].append(k)
                        pointIdxToLineIdxs[k].append(lineIdx)

        return max(len(pIdxs) for pIdxs in lineIdxToPointIdxs)

    def pointOnLine(self, point, line):
        p1, p2 = line
        # (point[0] - p1[0]) / (point[0] - p2[0]) = (point[1] - p1[1]) / (point[1] - p2[1])
        return (point.x - p1.x) * (point.y - p2.y) == (point.y - p1.y) * (point.x - p2.x)
