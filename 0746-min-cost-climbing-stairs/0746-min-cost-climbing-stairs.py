class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        #dp[i] = min cost to reach top
        # choices: 1 step, 2 steps 
    
        n = len(cost)
        prev = 0
        curr = 0
    
        for i in range(2, n+1):
            curr, prev = min(curr + cost[i-1], prev + cost[i-2]), curr
    
        return curr


        