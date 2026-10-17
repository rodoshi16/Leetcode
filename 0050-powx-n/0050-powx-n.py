class Solution:
    def myPow(self, x: float, n: int) -> float:
        #input: x, n
        # pow(), **
        # 2^3 = 2*2*2, x = 1/x
        # 

        def r(a, b):
            if b == 0:
                return 1 
            if b == 1:
                return a

            if b % 2 == 0:
                half = r(a, b // 2)
                res = half * half 
            else:
                half = r(a, (b - 1) // 2)
                res = half * half * a
            return res
        
      
        t = r(x, abs(n))
        if n < 0:
            return 1/t
        else:
            return t