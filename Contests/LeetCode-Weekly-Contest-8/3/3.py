"""
Problem:    417. Pacific Atlantic Water Flow
            https://leetcode.com/contest/8/problems/pacific-atlantic-water-flow/
Language:   Python 2
Result:     Accepted
"""

class Solution(object):
    def pacificAtlantic(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        if len(matrix) == 0 or len(matrix[0]) == 0:
            return []

        rowCount = len(matrix)
        colCount = len(matrix[0])
        self.matrix = matrix
        self.rowCount = rowCount
        self.colCount = colCount

        # handle Pacific
        toPacCells = []
        toPacCells.extend([(0, c) for c in xrange(colCount)])
        toPacCells.extend([(r, 0) for r in xrange(rowCount)])
        toPacCellsSet = self.findCellsByDFS(toPacCells)

        # handle Atlantic
        toAtlCells = []
        toAtlCells.extend([(rowCount - 1, c) for c in xrange(colCount)])
        toAtlCells.extend([(r, colCount - 1) for r in xrange(rowCount)])
        toAtlCellsSet = self.findCellsByDFS(toAtlCells)

        toBoth = toPacCellsSet & toAtlCellsSet
        return list(toBoth)

    def findCellsByDFS(self, initialCells):
        stack = initialCells
        toOceanCellsSet = set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while stack:
            cell = stack.pop()
            r, c = cell

            if cell in toOceanCellsSet:  # already accessed
                continue
            toOceanCellsSet.add(cell)

            for dr, dc in directions:
                adjR = r + dr
                adjC = c + dc

                if adjR < 0 or adjR >= self.rowCount or adjC < 0 or adjC >= self.colCount:
                    continue

                if self.matrix[adjR][adjC] >= self.matrix[r][c]:
                    stack.append((adjR, adjC))

        return toOceanCellsSet
