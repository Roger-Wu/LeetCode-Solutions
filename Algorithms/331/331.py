class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        charList = preorder.split(',')

        if len(charList) == 0:
            return False

        if charList[0] != '#':
            left = 1
            right = 1
        for char in charList[1:]:
            # check valid
            if left == 0 and right == 0:
                return False

            if char != '#':
                if left > 0: # now traversing left sub-tree
                    # left -= 1 += 1
                    right += 1
                else:
                    left += 1
                    # right -= 1 += 1
            else:
                if left > 0:
                    left -= 1
                else:
                    right -= 1

        if left == right == 0:
            return True
        else:
            return False
