class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        #m = len(nums2)
        nums1.extend(nums2)
        #nlogn + 0(m)
        nums1.sort()
        n = len(nums1)
        i = n // 2

        if n % 2 != 0:
            return nums1[i]
        else:
            return (nums1[i] + nums1[i-1]) / 2

