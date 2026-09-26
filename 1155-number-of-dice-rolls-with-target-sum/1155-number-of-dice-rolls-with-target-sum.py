class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        #no of ways to roll the dice so sum of face up numbers equals target

        memo = {}

        def recurse(n, target):
            count = 0 

            if target <  0:
                return 0
            elif n == 0 and target == 0:
                return 1
            elif n == 0 and target != 0:
                return 0
            elif (n, target) in memo:
                return memo[(n, target)]

            for i in range(1, k+1):
                count += recurse(n-1, target-i)
            
            memo[(n, target)] = count
            return count
    
        return recurse(n, target) % ((10**9)+7)
