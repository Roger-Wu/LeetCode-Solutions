"""
calc all sum of 2
then use hash table to implement 2-sum
O(nlogn + n^2 + n)
"""


class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        target = 0

        if len(nums) <= 2:
            return []

        nums.sort()

        sumOfTwo = dict()
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                s = nums[i]+nums[j]
                if s in sumOfTwo:
                    # sumOfTwo[s].append((i, j))  # may repeat

                    # if nums is [1, 1, 1, 2, 2]
                    # will only store (0, 1), (0, 3), (3, 4)
                    if nums[i] not in sumOfTwo[s]:  # avoid repeat
                        sumOfTwo[s][nums[i]] = (i, j)
                else:
                    sumOfTwo[s] = {nums[i]: (i, j)}

        triplets = []
        prev = nums[-1] + 1
        for k in xrange(len(nums)-1, -1, -1):  # from back to front, so k >= j
            if nums[k] == prev:
                continue

            comp = target - nums[k]
            if comp in sumOfTwo:
                for i, j in sumOfTwo[comp].values():
                    if k > j:
                        triplets.append((nums[i], nums[j], nums[k]))
            prev = nums[k]

        return triplets
