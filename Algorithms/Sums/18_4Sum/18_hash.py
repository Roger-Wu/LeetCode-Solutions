"""
O(nlogn + n^2 + n^2 + ?)
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if len(nums) <= 3:
            return []

        nums.sort()
        self.nums = nums

        sumFromLeft = dict()
        i = 0
        while i < len(nums):
            j = i+1
            while j < len(nums):
                s = nums[i] + nums[j]
                sumFromLeft.setdefault(s, [])
                sumFromLeft[s].append((i, j))
                j = self.moveRight(j)
            i = self.moveRight(i)

        sumFromRight = dict()
        l = len(nums)-1
        while l >= 0:
            k = l-1
            while k >= 0:
                s = nums[l] + nums[k]
                sumFromRight.setdefault(s, [])
                sumFromRight[s].append((k, l))
                k = self.moveLeft(k)
            l = self.moveLeft(l)

        quadruples = []
        for leftKey, leftPairs in sumFromLeft.iteritems():
            comp = target - leftKey
            if comp in sumFromRight:
                rightPairs = sumFromRight[comp]
                for i, j in leftPairs:
                    for k, l in rightPairs:
                        if j < k:
                            quadruples.append((nums[i], nums[j], nums[k], nums[l]))

        return quadruples

    def moveRight(self, index):
        index += 1
        while index < len(self.nums) and self.nums[index] == self.nums[index-1]:
            index += 1
        return index  # may be len(nums)

    def moveLeft(self, index):
        index -= 1
        while index >= 0 and self.nums[index] == self.nums[index+1]:
            index -= 1
        return index  # may be -1
