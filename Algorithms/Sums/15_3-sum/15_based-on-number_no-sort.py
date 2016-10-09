"""
calc all sum of 2
then use hash table to implement 2-sum
O(n^2 + n)
this is slower than the with sorting version
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

        # nums.sort()

        sumOfTwo = dict()
        for i in xrange(len(nums)):
            for j in xrange(i+1, len(nums)):
                s = nums[i]+nums[j]
                m = min(nums[i], nums[j])
                if s in sumOfTwo:
                    # sumOfTwo[s].append((i, j))  # may repeat

                    # if nums is [1, 1, 1, 2, 2]
                    # will only store (0, 1), (0, 3), (3, 4)
                    if m not in sumOfTwo[s]:  # avoid repeat
                        sumOfTwo[s][m] = (i, j)
                else:
                    sumOfTwo[s] = {m: (i, j)}

        triplets = set()
        usedNumsK = set()
        for k in xrange(len(nums)-1, -1, -1):  # from back to front, so k >= j
            if nums[k] in usedNumsK:
                continue

            comp = target - nums[k]
            if comp in sumOfTwo:
                for i, j in sumOfTwo[comp].values():
                    if k > j:
                        triplets.add(tuple(sorted([nums[i], nums[j], nums[k]])))
            usedNumsK.add(nums[k])

        return list(triplets)
