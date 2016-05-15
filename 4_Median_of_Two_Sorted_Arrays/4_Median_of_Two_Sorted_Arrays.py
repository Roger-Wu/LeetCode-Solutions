class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        l1 = len(nums1)
        l2 = len(nums2)

        if l1 == 0:
            return self.median(nums2)
        if l2 == 0:
            return self.median(nums1)
        
        print l1, l2
        return nums1[l1/2]

    def median(self, arr):
        l = len(arr)
        if l % 2 == 0:
            return (arr[l/2-1] + arr[l/2]) / 2.0
                return float(arr[l/2])
        return float(arr[l/2])
