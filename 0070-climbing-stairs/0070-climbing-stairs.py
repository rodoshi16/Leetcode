class Solution: 
    def climbStairs(self, n: int) -> int:

        d = {0: 0, 1: 1, 2: 2}

        def recurse(n):
            if n in d:
                return d[n]
            else:
                val = recurse(n-1) + recurse(n-2)
                d[n] = val
                return val
        
        return recurse(n)


    