class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0 

        prev = 0 
        curr = 1 

        for i in range(2, n+1):
            prev, curr = curr, curr + prev
        
        return curr


        
