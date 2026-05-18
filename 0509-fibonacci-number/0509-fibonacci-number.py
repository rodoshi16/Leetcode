class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}
        c = 0 
        if n in memo:
            c += memo[n]
        else:
            c += self.fib(n-1) + self.fib(n-2)
            memo[n] = c
        
        return c
