class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # idea 1: from smallest number
        #     wrong, counter ex: 1 2 3 100

        # idea 2: from the one that can earn you most coins:
        #     wrong, counter ex: 1 2 100 2 1

        self.calced = dict()
        return self.maxAdd(1, 1, nums)

    def maxAdd(self, left, right, nums):
        if len(nums) == 0:
            return 0

        # calced = self.checkCalced(left, right, nums)
        calced = self.calced.get( str(left) + ',' + str(right) + ',' + str(nums) , None)
        if calced is not None:
            return calced

        maxCoins = 0
        for i in xrange(len(nums)):
            coins = nums[i]*left*right + self.maxAdd(left, nums[i], nums[:i]) + self.maxAdd(nums[i], right, nums[i+1:])
            maxCoins = max(maxCoins, coins)

        # self.setCalced(left, right, nums, maxCoins)
        self.calced[ str(left) + ',' + str(right) + ',' + str(nums) ] = maxCoins
        return maxCoins

    def setCalced(self, left, right, nums, result):
        self.calced[ str(left) + ',' + str(right) + ',' + str(nums) ] = result

    def checkCalced(self, left, right, nums):
        return self.calced.get( str(left) + ',' + str(right) + ',' + str(nums) , None)

    def toUniqueString(self, left, right, nums):
        return str(left) + ',' + str(right) + ',' + str(nums)
