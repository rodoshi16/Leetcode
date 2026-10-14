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

       
        dp = costs[0][:]
        n = len(costs)


        for i in range(1, n):
            lst = []
            for j in range(3):
                prev_min = math.inf
                for k in range(3):
                    if k != j:
                        prev_min = min(prev_min, dp[k])
            
                lst.append(costs[i][j] + prev_min)
            dp = lst
        
        return min(dp)

       













        




      



            
            
        
    
            





