from bisect import bisect_left, bisect_right

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        l = len(nums)

        nums.sort()

        bestSum = nums[0] + nums[1] + nums[2]
        bestDiff = abs(bestSum - target)

        sortedSumsOfTwo = []
        for i1 in xrange(l):
            sumsOfTwo = []
            for i2 in xrange(i1, l):
                sumsOfTwo.append( (nums[i1] + nums[i2], i1, i2) )
            print sumsOfTwo
            sortedSumsOfTwo = merge(sortedSumsOfTwo, sumsOfTwo)

        print sortedSumsOfTwo

        i3 = l - 1
        for sot, i1, i2 in sortedSumsOfTwo:
            print sot, i1, i2
            currSum = sot + nums[i3]
            currDiff = abs(currSum - target)
            while True:
                if i3 - 1 <= i2:
                    break

                nextSum = sot + nums[i3-1]
                nextDiff = abs(nextSum - target)
                if nextDiff < currDiff:
                    currSum = nextSum
                    currDiff = nextDiff
                    i3 -= 1
                    continue
                else:
                    break

            if i3 <= i2:
                break

            if currDiff < bestDiff:
                bestSum = currSum
                bestDiff = currDiff

            if bestDiff == 0:
                return bestSum

        return bestSum


        # l = len(nums)
        # bestSum = nums[0] + nums[1] + nums[2]
        # bestDiff = abs(bestSum - target)
        # for i1 in xrange(l):
        #     for i2 in xrange(i1, l):
        #         for i3 in xrange(i2, l):
        #             s = nums[i1] + nums[i2] + nums[i3]
        #             diff = abs(s - target)
        #             if diff < bestDiff:
        #                 bestSum = s
        # return bestSum


def merge(a1, a2):
    l1 = len(a1)
    l2 = len(a2)
    i1 = 0
    i2 = 0
    merged = []

    while i1 < l1 and i2 < l2:
        if a1[i1][0] < a2[i2][0]:
            merged.append(a1[i1])
            i1 += 1
        else:
            merged.append(a2[i2])
            i2 += 1
    if i1 < l1:
        merged.extend(a1[i1:])
    else:
        merged.extend(a2[i2:])

    return merged

s = Solution()
print s.threeSumClosest([1,1,1,0], 100)
