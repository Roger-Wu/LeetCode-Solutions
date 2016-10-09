# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        zigzag = []
        currLevelNodes = [root]
        level = 0
        while currLevelNodes:
            zigzag.append([node.val for node in currLevelNodes])
            nextLevelNodes = []
            while currLevelNodes:
                node = currLevelNodes.pop()
                if level % 2 == 0:
                    if node.right:
                        nextLevelNodes.append(node.right)
                    if node.left:
                        nextLevelNodes.append(node.left)
                else:
                    if node.left:
                        nextLevelNodes.append(node.left)
                    if node.right:
                        nextLevelNodes.append(node.right)
            currLevelNodes = nextLevelNodes
            level += 1
        return zigzag
