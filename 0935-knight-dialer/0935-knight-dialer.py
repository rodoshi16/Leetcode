class Solution:
    def knightDialer(self, n: int) -> int:
        #2 up 1 r
        # 2 up 1 l
        # 2 down 1 r 
        # 2 down 1 l
        # 2 right 1 up
        # 2 right 1 down
        # 2 left 1 up
        # 2 left 1 down

        # (3, 0), (3, 3) - cannot acess
        # how many distinct phone numbers of length n 

        # 16, 18, 83, 81, 67, 76, 37, 73
        # base case: if out of bounds - 0
        # each recurse - decrease n, n == 0 -> 1
        # cache recursive calls

        d = {}

        def recurse(k, r, c):
            if not(0 <= r < 4) or not(0 <= c < 3) or (3, 0) == (r, c) or (3,2) == (r, c):
                return 0 
            
            if k == 0:
                return 1

            state = (k, r, c)

            if state in d:
                return d[state]
            
            count = 0 
            count += recurse(k-1, r+2, c-1)
            count += recurse(k-1, r+2, c+1)

            count += recurse(k-1, r-2, c-1)
            count += recurse(k-1, r-2, c+1)

            count += recurse(k-1, r+1, c+2)
            count += recurse(k-1, r-1, c+2)

            count += recurse(k-1, r+1, c-2)
            count += recurse(k-1, r-1, c-2)


            d[state] = count % ((10**9)+ 7)
            return count % ((10**9)+ 7)

        
        total = 0 
        for i in range(4):
            for j in range(3):
                if (i, j) != (3, 0) and (i, j) != (3, 2):
                    total += recurse(n-1, i, j)
        return total % ((10**9)+ 7)
        
        




