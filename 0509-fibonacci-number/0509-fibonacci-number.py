class Solution:
    def fib(self, n: int) -> int:
        memo = {0:0, 1:1}

        def f(n):
            if n in memo:
                return memo[n]
            else:
                memo[n] = self.fib(n-1) + self.fib(n-2)

            return memo[n]
        return f(n)
