"""
O(n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        d = dict()
        for i in xrange(len(nums)):
            complement = target - nums[i]
            # if d.get(compensate) is not None:
            if complement in d:
                return (d[complement], i)
            d[nums[i]] = i
