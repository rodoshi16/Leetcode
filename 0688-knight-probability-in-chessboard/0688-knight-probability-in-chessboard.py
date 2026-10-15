class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        #2 up, l r 
        # 2 down, l r 
        # 2 right, u d
        # 2 left, u d

        # k moves, moved off the chessboard
        # no of branches where pos within board

        # cache with every pos and 

        count = 0 
        d = {}

        def recurse(moves, r, c):
            if not(0 <= r < n) or not(0 <= c < n):
                return 0
            
            if moves == 0:
                return 1 
            
            state = (moves, r, c)

            if state in d:
                return d[state]
    
            count = 0 

            count += recurse(moves-1, r+2, c+1)
            count += recurse(moves-1, r+2, c-1)

            count += recurse(moves-1, r-2, c+1)
            count += recurse(moves-1, r-2, c-1)

            count += recurse(moves-1, r+1, c-2)
            count += recurse(moves-1, r-1, c-2)

            count += recurse(moves-1, r+1, c+2)
            count += recurse(moves-1, r-1, c+2)

            d[state] = count
            return count

        
        fav = recurse(k, row, column)
        return fav / (8**k)