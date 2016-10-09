"""
3 pointers
1st pointer will be leftmost
2nd and 3rd pointers are used for 2-sum
O(nlogn + n^2)
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
        self.nums = nums

        triplets = []
        i = 0
        while i < len(nums):
            low = i+1
            high = len(nums)-1
            tempTarget = target - nums[i]
            while low < high:
                s = nums[low] + nums[high]
                if s == tempTarget:
                    triplets.append((nums[i], nums[low], nums[high]))
                    low = self.moveRight(low)
                    high = self.moveLeft(high)
                elif s < tempTarget:
                    low = self.moveRight(low)
                else:
                    high = self.moveLeft(high)
            i = self.moveRight(i)

        return triplets

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
