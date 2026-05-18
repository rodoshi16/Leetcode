class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        dp = [0] * len(nums)
        n = len(nums)
        m = max(nums[0], nums[1])
        dp[0] = nums[0]
        dp[1] = m

        for i in range(2, n):
            dp[i] = max(dp[i-1], dp[i-2]+ nums[i])
            if dp[i] > m:
                m = dp[i]
        
        return m
        

