class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        # n by n 
        # (0,0)

        # 2 up, 1 r l
        # 2 down, 1 r l
        # 2 right, 1 up d
        # 2 left, 1 dw up

        # remains on board: pos needs to be in range rc
        # moves == 0

        # 2 moves 
        # 1 -> 8 choices 
        # 8^2

        d = {}

        def recurse(moves, r, c):
            if not (0 <= r < n) or not (0 <= c < n):
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

            d[state] = count
            return count

        fav = recurse(k, row, column)
        return fav/(8**k)