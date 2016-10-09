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

        # 0 ~ n+1 = 0~i + i~n+1
        #


        # 0~2, 1~3, ... (l-1)~(l+1)  # width = 1
        # 0~3, 1~4, ..., (l-2)~(l+1)
        # ...
        # 0~l, 1~(l+1)
        # 0~(l+1) # width = l

        l = len(nums)
        nums.insert(0, 1)
        nums.append(1)
        print nums

        maxCoinsBetween = [[0]*i for i in xrange(l+1, 0, -1)]
        # maxCoinsMatrix[width][left] # [1][0]

        for left in xrange(l):
            maxCoinsBetween[1][left] = nums[left] * nums[left+1] * nums[left+2]

        for width in xrange(2, l+1):
            for left in xrange(0, l+1-width):
                right = left + width + 1
                for mid in xrange(left+1, right):
                    maxCoinsBetween[width][left] = max(maxCoinsBetween[width][left],
                        nums[left] * nums[mid] * nums[right] + maxCoinsBetween[mid-left-1][left] + maxCoinsBetween[right-mid-1][mid])
        return maxCoinsBetween[l][0]

        
