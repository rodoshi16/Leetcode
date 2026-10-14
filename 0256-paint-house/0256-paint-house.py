import math
class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        #3 choices: red, blue, green
        # return min cost to paint all houses

        # [[17,2,17],[16,16,5],[14,3,19]]
        # [[171, 80, 171], [9, 8, 56], [6, 9, 51]]

        # keep track of prev- dependency
        # greedy 

        # [17, 2, 18], [98, 3, 85], [90, 90, 1]
        # i need to know all possible paths

        # dp[i] = min cost of house at index i, remember the color or the index

        dp = []
        n = len(costs)
        for i in range(n):
            dp.append([0] * 3)
        
        dp[0] = costs[0][:]

        for i in range(1, n):
            for j in range(3):
                prev_min = math.inf
                for k in range(3):
                    if k != j:
                        prev_min = min(prev_min, dp[i-1][k])

                dp[i][j] = costs[i][j] + prev_min
        
        return min(dp[n-1])

       













        




      



            
            
        
    
            





