"""
Problem:    416. Partition Equal Subset Sum
            https://leetcode.com/contest/8/problems/partition-equal-subset-sum/
Language:   Python 2
Result:     Accepted
Reference:  https://en.wikipedia.org/wiki/Partition_problem
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False

        halfSum = totalSum / 2
        canSum = set([0])
        for num in nums:
            for cs in list(canSum):  # avoid set size changing during iteration
                canSum.add(cs + num)
            if halfSum in canSum:
                return True

        return (halfSum in canSum)
