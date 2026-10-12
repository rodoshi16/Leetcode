class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # 2 choices - right or down
        # branches that lead to end += 1 

        d = {}

        def recurse(a, b):
            if a >= m or b >= n:
                return 0
    
            if a == m - 1 and b == n - 1:
                return 1 
            
            if (a+1, b) in d:
                right = d[(a+1, b)]
            else:
                right =  recurse(a+1, b)
                d[(a+1, b)] = right
            
            if (a, b+1) in d:
                down = d[(a, b+1)]
            else:
                down =  recurse(a, b+1)
                d[(a, b+1)] = down
            return right + down 
        
        return recurse(0, 0)

        