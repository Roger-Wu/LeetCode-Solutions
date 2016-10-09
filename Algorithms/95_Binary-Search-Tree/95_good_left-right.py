# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        return self.genTrees(1, n)

    def genTrees(self, begin, end):
        if begin > end:
            return [None]

        trees = []
        for rootVal in xrange(begin, end+1):
            leftTrees = self.genTrees(begin, rootVal-1)
            rightTrees = self.genTrees(rootVal+1, end)
            for leftTree in leftTrees:
                for rightTree in rightTrees:
                    root = TreeNode(rootVal)
                    root.left = leftTree
                    root.right = rightTree
                    trees.append(root)
        return trees
