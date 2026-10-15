class Solution:
    def knightDialer(self, n: int) -> int:
        # no of recursive calls - n 

        d = {}

        def recurse(moves, r, c):
            if not (0 <= r < 4) or not (0 <= c < 3) or (r, c) == (3, 0) or (r, c) == (3, 2):
                return 0 

            if moves == 0:
                return 1 
            
            state = (moves, r, c)

            if state in d:
                return d[state]

            count = 0 
            count += recurse(moves-1, r-2, c+1)
            count += recurse(moves-1, r-2, c-1)

            count += recurse(moves-1, r+2, c+1)
            count += recurse(moves-1, r+2, c-1)

            count += recurse(moves-1, r-1, c+2)
            count += recurse(moves-1, r+1, c+2)

            count += recurse(moves-1, r-1, c-2)
            count += recurse(moves-1, r+1, c-2)

            d[state] = count % ((10**9)+7)
            return count

        total = 0
        for r in range(4):
            for c in range(3):
                if (r, c) != (3, 0) and (r, c) != (3, 2):
                    total += recurse(n - 1, r, c)
        
        return total % ((10**9)+7)
        