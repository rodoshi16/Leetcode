class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        #go through border if find 0 -> t 
        # nested loop -> turn into 0 into X

        n = len(board)
        m = len(board[0])

        dir = [[1, 0], [0, -1], [0, 1], [-1, 0]]

        def dfs(i, j):
            if i < 0 or i >= n or j < 0 or j >= m or board[i][j] != "O":
                return 
            
            board[i][j] = "t"
            
            for d in dir:
                dfs(i + d[0], j+ d[1])
            


        for i in range(m):
            if board[0][i] == "O":
                dfs(0, i)
            
            if board[n-1][i] == 'O':
                dfs(n-1, i)

        
        for j in range(n):
            if board[j][0] == "O":
                dfs(j, 0)
            
            if board[j][m-1] == "O":
                dfs(j, m-1)
       

        for i in range(n):
            for j in range(m):
                if board[i][j] == 'O':
                    board[i][j] = 'X'
                elif board[i][j] == 't':
                    board[i][j] = 'O'

        

        


        
