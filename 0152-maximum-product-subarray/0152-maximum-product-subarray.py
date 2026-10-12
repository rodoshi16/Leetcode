class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        #input: nums
        # out: int 

        # pos: sum all
        # [-1, -2, -3, -4]
        # [2, 3, -2, 4]
        # dp[i] = max(dp[i-1] * nums[i], nums[i])
        # [2, -4, 3, -2]

        # -ve numbers can make 

        n = len(nums)
        max_a = [0] * n 
        min_a = [0] * n 
        max_a[0] = nums[0]
        min_a[0] = nums[0]

        for i in range(1, len(nums)):
            max_a[i] = max(nums[i], max_a[i-1]*nums[i], min_a[i-1]*nums[i])
            min_a[i] = min(nums[i], max_a[i-1]*nums[i], min_a[i-1]*nums[i])
    
        return max(max_a)












