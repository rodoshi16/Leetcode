class Solution:
    def fib(self, n: int) -> int:
        count = 0 
        if n == 0:
            return 0 
        elif n == 1:
            return 1
        else: 
            count += self.fib(n-1) + self.fib(n-2)
        return count

        




        