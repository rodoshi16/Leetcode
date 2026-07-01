class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [["."] * n for _ in range(n)]

        r = []
        c = []
        d = []
        res = []

        def backtrack(i, j, queens):
            if queens == n:
                res.append(["".join(row) for row in board])
                return

            if i == n:
                return

            # move to next cell
            next_i = i
            next_j = j + 1

            if next_j == n:
                next_i += 1
                next_j = 0

            # option 1: don't place queen here
            backtrack(next_i, next_j, queens)

            # option 2: place queen here
            if (i not in r) and (j not in c) and ((i, j) not in d):
                board[i][j] = "Q"
                r.append(i)
                c.append(j)

                old_len = len(d)

                # mark diagonals
                x, y1, y2 = i, j, j
                while x + 1 < n:
                    x += 1
                    y1 += 1
                    y2 -= 1
                    d.append((x, y1))
                    d.append((x, y2))

                backtrack(next_i, next_j, queens + 1)

                # undo diagonals
                while len(d) > old_len:
                    d.pop()

                # undo queen
                board[i][j] = "."
                r.pop()
                c.pop()

        backtrack(0, 0, 0)
        return res
        # lst = []
        # for _ in range(n):
        #     lst.append(["."]* n)
            
        # r = []
        # c = []
        # d = []
        # res = []
        # def backtrack(i, j, queens):
        #     if queens == n:
        #         res.append(lst[:])
        #         return 1
            
        #     if i == n:
        #         return 

        #     for i in range(len(lst)):
        #         for j in range(len(lst)):
            
        #             if (i not in r) and (j not in c) and (i, j) not in d:
        #                 lst[i][j] = "Q"
        #                 r.append(i)
        #                 c.append(j)


        #                 left, right = i, j
        #                 right2 = j
        #                 while right < n-1 and left < n-1:
        #                     left += 1
        #                     right += 1
        #                     right2 -= 1
        #                     d.append((left, right))
        #                     d.append((left, right2)) 
                        
                        
        #                 backtrack(i, j+1, queens+1)
        #                 lst[i][j] = "."

        #                 if d:
        #                     d.pop()
        #                 r.pop()
        #                 c.pop()
        
        # backtrack(0, 0, 0)
        # return res
            