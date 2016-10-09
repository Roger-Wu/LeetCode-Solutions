# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        wrongNodesPair = []

        nodes = [root]
        prevVal =
        while nodes:
            node = nodes.pop()
            prevVal =
            if node.left:
                nodes.append(node.left)
                if node.left.val > node.val:
                    wrongNodes.append((node,0))
            if node.right:
                nodes.append(node.right)
                if node.right.val < node.val:
                    wrongNodes.append((node,1))


        if len(wrongNodes) == 1:
            node, lr = wrongNodes[0]
            if lr == 0:
                node.val, node.left.val = node.left.val, node.val
            else:
                node.val, node.right.val = node.right.val, node.val
        else:
            if wrongNodes[0][1] == 0:
                node1 = wrongNodes[0][0].left
            else:
                node1 = wrongNodes[0][0].right

            if wrongNodes[1][1] == 0:
                node2 = wrongNodes[1][0].left
            else:
                node2 = wrongNodes[1][0].right

            node1.val, node2.val = node2.val, node1.val

        # print wrongNodes
