class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #dp[i] = min cost to reach top
        # choices: 1 step, 2 steps 
    
        n = len(cost)
        memo = {0: 0, 1:0}

        def dp(i):
            if i in memo:
                return memo[i]

            else:
                memo[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2]) 
                return memo[i]
        
        return dp(n)


        