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

        quadruples = []
        i = 0
        while i < len(nums):
            low = i+1
            high = len(nums)-1
            tempTarget = target - nums[i]
            while low < high:
                s = nums[low] + nums[high]
                if s == tempTarget:
                    quadruples.append((nums[i], nums[low], nums[high]))
                    low = self.moveRight(low)
                    high = self.moveLeft(high)
                elif s < tempTarget:
                    low = self.moveRight(low)
                else:
                    high = self.moveLeft(high)
            i = self.moveRight(i)

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
