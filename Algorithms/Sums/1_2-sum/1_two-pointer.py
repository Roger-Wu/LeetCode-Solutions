"""
O(nlogn + n)
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        sortedIdx = sorted(range(len(nums)), key=lambda k: nums[k])
        nums.sort()
        # sortedNums = sorted(nums)

        left = 0
        right = len(nums) - 1
        while left < right:
            s = nums[left] + nums[right]
            if s == target:
                return (sortedIdx[left], sortedIdx[right])
            elif s < target:
                left += 1
            else:
                right -= 1
        return None
