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
        j = 0
        while j < len(nums):
            i = 0
            while i < j:
                s = nums[i] + nums[j]
                sumFromLeft.setdefault(s, [])
                sumFromLeft[s].append((i, j))  # will be naturally sorted by j
                i = self.moveRight(i)
            if j+1 < len(nums):
                if nums[j] == nums[j+1]:
                    s = nums[j] + nums[j+1]
                    sumFromLeft.setdefault(s, [])
                    sumFromLeft[s].append((j, j+1))
            j = self.moveRight(j)

        sumFromRight = dict()
        k = len(nums)-1
        while k >= 0:
            l = len(nums)-1
            while l > k:
                s = nums[l] + nums[k]
                sumFromRight.setdefault(s, [])
                sumFromRight[s].append((k, l))  # reversedly sorted by k
                l = self.moveLeft(l)
            if k-1 >= 0:
                if nums[k] == nums[k-1]:
                    s = nums[k] + nums[k-1]
                    sumFromRight.setdefault(s, [])
                    sumFromRight[s].append((k-1, k))
            k = self.moveLeft(k)

        quadruples = []
        for leftKey, leftPairs in sumFromLeft.iteritems():
            comp = target - leftKey
            if comp in sumFromRight:
                rightPairs = sumFromRight[comp]
                for i, j in leftPairs:
                    for k, l in rightPairs:
                        if j < k:
                            quadruples.append((nums[i], nums[j], nums[k], nums[l]))
                        else:
                            break

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
