class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]
            
        elif n == 0:
            return 0
        
        def r(lst):
            n = len(lst)

            if n == 1:
                return lst[0]
            
            elif n == 0:
                return 0

            dp = [0] * n
            dp[0] = lst[0]


            dp[1] = max(lst[0], lst[1])
            
            for i in range(2, n):
                dp[i] = max(dp[i-1], dp[i-2]+lst[i])
            
            return dp[n-1]
        
        return max(r(nums[1:]), r(nums[:-1]))

     