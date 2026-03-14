class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        row = len(grid)
        col = len(grid[0])
        island = 0 
        visited = set()
        
        def dfs(i, j):
            visited.add((i, j))
            directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
            for d in directions:
                dr = i + d[0] 
                dc = j + d[1]
                if 0 <= dr < row and 0 <= dc <col and grid[dr][dc] == "1" and (dr,dc) not in visited:
                    dfs(dr, dc)
            return
        
        for i in range(row):
            for j in range(col):
                if grid[i][j] == "1" and (i,j) not in visited:
                    island += 1 
                    dfs(i, j)
        return island 

                    
        
                




        