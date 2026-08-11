class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        n = len(nums1)
        m = len(nums2)
        half = (n + m +1) // 2

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n
        
        l = 0
        r = len(nums1)

        while l <= r:
            i = (l + r) // 2
            j = half - i 

            #boundary values

            if i == 0:
                A_left = float('-inf')
            else:
                A_left = nums1[i - 1]

            if i == n:
                A_right = float('inf')
            else:
                A_right = nums1[i]

            if j == 0:
                B_left = float('-inf')
            else:
                B_left = nums2[j - 1]

            if j == m:
                B_right = float('inf')
            else:
                B_right = nums2[j]


            if A_left > B_right:
                r = i - 1 
            elif B_left > A_right:
                l = i + 1
            else:

                if (n+m) % 2 != 0:
                    return max(A_left, B_left)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2

