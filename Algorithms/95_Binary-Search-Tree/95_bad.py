# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from copy import copy

def copyTree(tree):
    newRoot = copy(tree)
    queue = [newRoot]
    while queue:
        node = queue.pop()
        if node.left:
            newLeft = copy(node.left)
            queue.append(newLeft)
            node.left = newLeft
        if node.right:
            newRight = copy(node.right)
            queue.append(newRight)
            node.right = newRight
    return newRoot

def upliftNodes(tree, n):
    if not tree:
        return tree
    newTree = copyTree(tree)

    queue = [newTree]
    while queue:
        node = queue.pop()
        node.val += n
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
    return newTree

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        if n == 0:
            return []

        trees = [[None]]
        for size in xrange(1, n+1):
            thisSizeTrees = []
            for leftSize in xrange(size):
                rightSize = (size - 1) - leftSize
                for leftTree in trees[leftSize]:
                    for rightTree in trees[rightSize]:
                        root = TreeNode(leftSize+1)
                        root.left = leftTree
                        root.right = upliftNodes(rightTree, leftSize+1)
                        thisSizeTrees.append(root)
            trees.append(thisSizeTrees)

        return trees[n]
        
