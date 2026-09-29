class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #choices: 1 step or 2 steps
        #state: what tells where i am 
        # dp[i] = min cost to climb top

        # i -> i-1 , i-2
        # min(i-1, i-2)
    
        n = len(cost)

        dp = [0] * (n+1)

        for i in range(2, n+1):
            dp[i] = min(cost[i-1] + dp[(i-1)], cost[i-2] + dp[(i-2)])
        
        return dp[n]