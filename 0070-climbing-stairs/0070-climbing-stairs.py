class Solution: 
    def climbStairs(self, n: int) -> int:

        prev = 1
        curr = 2 

        if n == 1:
            return 1
        elif n == 2:
            return 2 
        else:
            for i in range(3, n+1):
                val = curr + prev
                prev = curr
                curr = val

            return curr
            

    