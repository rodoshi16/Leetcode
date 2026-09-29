class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #choices: 1 step or 2 steps
        #state: what tells where i am 
        # dp[i] = min cost to climb top

        # i -> i-1 , i-2
        # min(i-1, i-2)
    
        n = len(cost)
        memo = {0:0, 1:0}

        def min_cost(i):

            if i in memo:
                return memo[i]
            else: 
                memo[i] = min(cost[i-1] + min_cost(i-1), cost[i-2] + min_cost(i-2))
            
            return memo[i]

        return min_cost(n)