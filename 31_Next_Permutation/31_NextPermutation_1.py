class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        """
        iterate the nums backward
        if nums[i-1] < nums[i]:

        524 1 3 -> 524 3 1
        52 3 41 -> 52 4 13
        5 2 431 -> 5 3 124
        5 2 4433221 -> 5 3 1222344
        """
        if len(nums) < 2:
            return
        reversedTail = []
        reversedTail.append(nums.pop())
        while len(nums) > 0:
            last = nums.pop()
            if last >= reversedTail[-1]:
                reversedTail.append(last)
            else:
                for i in xrange(len(reversedTail)):
                    if reversedTail[i] > last:
                        newHead = reversedTail[i]
                        reversedTail[i] = last
                        reversedTail.insert(0,newHead)
                        break
                break

        nums.extend(reversedTail)

        
