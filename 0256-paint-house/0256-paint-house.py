import math
class Solution:
    def minCost(self, costs: list[list[int]]) -> int:
        # r    b     g 
    # 0  17   2     17
    # 1 16+2. 16+17, 5+2
    # 2  14+,   3+.  19+

    #cost[i][j] + previous min
 
    # 3 choices: red, blue, green (0, 1, 2)
    # [[17,2,17],[16,16,5],[14,3,19]]
    # min cost
    # 2 adj houses cannot be the same color

    # [15, 17, 3], [80, 90, 1], [2, 50, 50]
    # 18

    # greedy doesnt work 
    # 2^n 

    # dp[i] = min cost at ith pos
    # remember prev color
    # decisions are not indepedent
    # cost, color 

        n = len(costs)
        
        dp = costs[0][:]

        for i in range(1, n):
            lst = []
            for j in range(3):
                prev_min = math.inf
                for k in range(3):
                    if j != k:
                        prev_min = min(prev_min, dp[k])
                
                lst.append(costs[i][j] + prev_min)
            dp = lst

        return min(dp)


        










        




      



            
            
        
    
            





