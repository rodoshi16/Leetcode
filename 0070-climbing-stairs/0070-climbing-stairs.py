class Solution:
    def climbStairs(self, n: int) -> int:
        prev = 1
        curr = 2

        if n == 1:
            return 1 
        elif n == 2:
            return 2
        else: 
            for i in range(2, n):
                prev, curr = curr, prev+curr

        return curr




    