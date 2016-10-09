"""
calc sum of 2
then use hash table to implement 2-sum
O(n^2 + n)
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0

        sumOfTwoDict = dict()
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                s = nums[i]+nums[j]
                if s in sumOfTwoDict:
                    sumOfTwoDict[s].append((s, i, j))
                else:
                    sumOfTwoDict[s] = [(s, i, j)]

        triplets = []
        for k in xrange(len(nums)):
            # k must > j
            comp = target - nums[k]
            if comp in sumOfTwoDict:
                for s, i, j in sumOfTwoDict[comp]:
                    if k > j:
                        triplets.append((nums[i], nums[j], nums[k]))

        return triplets
