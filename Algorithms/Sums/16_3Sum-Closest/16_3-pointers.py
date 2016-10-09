"""
3 pointers
1st pointer will be leftmost
2nd and 3rd pointers are used for 2-sum
O(nlogn + n^2)
"""


class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 2:
            return []

        nums.sort()
        self.nums = nums

        bestDiff = abs(nums[0] + nums[1] + nums[2] - target)
        bestSum = nums[0] + nums[1] + nums[2]
        i = 0
        while i < len(nums):
            low = i+1
            high = len(nums)-1
            tempTarget = target - nums[i]
            while low < high:
                s = nums[low] + nums[high]
                if s == tempTarget:
                    return target
                elif s < tempTarget:
                    diff = tempTarget - s
                    if diff < bestDiff:
                        bestDiff = diff
                        bestSum = nums[i] + s
                    low = self.moveRight(low)
                else:
                    diff = s - tempTarget
                    if diff < bestDiff:
                        bestDiff = diff
                        bestSum = nums[i] + s
                    high = self.moveLeft(high)
            i = self.moveRight(i)

        return bestSum

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
