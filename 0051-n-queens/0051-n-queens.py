class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        res = []
        lst = []
        for i in range(n):
            lst.append(["."]*n)

        c = set()
        d1 = set()
        d2 = set()

        def backtrack(q, row, lst):
            if n == q:
                res.append(["".join(row) for row in lst])
                return 
            
            for col in range(n):
                if col not in c and (row+col) not in d1 and (row-col) not in d2:
                    lst[row][col] = "Q"
                    c.add(col)

    
                    d1.add(row+col)
                    d2.add(row-col)

                    backtrack(q+1, row+1, lst)

                    lst[row][col] = "."
                    c.remove(col)
                    d1.remove(row+col)
                    d2.remove(row-col)


        backtrack(0, 0, lst)
        return res














