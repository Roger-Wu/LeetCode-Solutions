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

        for i in xrange(len(nums)-1, 0, -1):
            if nums[i-1] < nums[i]:
                for j in xrange(len(nums)-1, i-1, -1):
                    if nums[j] > nums[i-1]:
                        nums[i-1], nums[j] = nums[j], nums[i-1]
                        nums[i:] = reversed(nums[i:])
                        return

        nums.reverse()
